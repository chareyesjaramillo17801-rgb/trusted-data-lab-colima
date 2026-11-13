"""Análisis complementario reproducible de E1, sin modificar Bronce."""
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing, Holt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'data' / 'oro'

def run():
    datos = pd.read_parquet(ROOT / 'data/plata/shf_colima.parquet')
    registros = pd.read_parquet(ROOT / 'data/plata/sniiv.parquet')
    resultados, pronosticos = [], []
    for municipio in ('Manzanillo', 'Villa de Álvarez'):
        d = datos.loc[datos['Municipio'].eq(municipio)].sort_values(['Año', 'Trimestre'])
        y = pd.Series(d['Indice'].to_numpy(dtype=float))
        if len(y) < 24 or not np.isfinite(y).all():
            raise ValueError(f'Serie insuficiente o inválida: {municipio}')
        train, test = y.iloc[:-8], y.iloc[-8:]
        candidatos = {
            'Holt': lambda train=train: Holt(train, initialization_method='estimated').fit(),
            'Holt-Winters': lambda train=train: ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=4, initialization_method='estimated').fit(),
            'ARIMA(1,1,1)': lambda train=train: ARIMA(train, order=(1,1,1)).fit(),
        }
        evaluados = []
        for nombre, crear in candidatos.items():
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    ajuste = crear()
                pred = np.asarray(ajuste.forecast(8), dtype=float)
                mae = float(np.mean(np.abs(test.to_numpy()-pred)))
                evaluados.append((mae, nombre))
            except (ValueError, np.linalg.LinAlgError) as exc:
                resultados.append({'municipio': municipio, 'modelo': nombre, 'error': str(exc)})
        if not evaluados:
            raise RuntimeError(f'No se pudo ajustar ningún modelo para {municipio}')
        _, mejor = min(evaluados)
        # Reentrenar con toda la serie SOLO después de seleccionar con prueba retenida.
        if mejor == 'Holt':
            ajuste_final = Holt(y, initialization_method='estimated').fit()
        elif mejor == 'Holt-Winters':
            ajuste_final = ExponentialSmoothing(y, trend='add', seasonal='add', seasonal_periods=4, initialization_method='estimated').fit()
        else:
            ajuste_final = ARIMA(y, order=(1,1,1)).fit()
        residuos = np.asarray(ajuste_final.resid, dtype=float)
        residuos = residuos[np.isfinite(residuos)]
        ljung = float(acorr_ljungbox(residuos, lags=[min(8, max(1,len(residuos)//5))], return_df=True)['lb_pvalue'].iloc[0])
        decomp = seasonal_decompose(y, model='additive', period=4, extrapolate_trend='freq')
        p_adf = float(adfuller(y, autolag='AIC')[1])
        p_diff = float(adfuller(y.diff().dropna(), autolag='AIC')[1])
        pred_fut = np.asarray(ajuste_final.forecast(4),dtype=float)
        # Intervalos empíricos aproximados, no intervalos calibrados de predicción.
        sigma = float(np.std(residuos,ddof=1))
        ultimo = pd.Period(year=int(d['Año'].iloc[-1]),quarter=int(d['Trimestre'].iloc[-1]),freq='Q')
        for h, valor in enumerate(pred_fut, 1):
            pronosticos.append({'municipio':municipio,'periodo':str(ultimo+h),'modelo':mejor,'pronostico':float(valor),'banda_inferior_aproximada':float(valor-1.96*sigma*np.sqrt(h)),'banda_superior_aproximada':float(valor+1.96*sigma*np.sqrt(h)),'metodo_banda':'heurística residual 1.96*sigma*sqrt(h); no calibrada'})
        resultados.append({'municipio':municipio,'modelo_elegido':mejor,'mae_validacion':min(evaluados)[0],'observaciones':len(y),'adf_p_nivel':p_adf,'adf_p_primera_diferencia':p_diff,'ljung_box_p_residuos':ljung,'descomposicion_tendencia_final':float(decomp.trend.iloc[-1]),'descomposicion_estacional_ultimo':float(decomp.seasonal.iloc[-1]),'residuos_desviacion':sigma})
    # Transformaciones para análisis, SIN sustituir las unidades originales.
    s = registros.copy()
    s['viviendas_zscore'] = s.groupby('municipio')['viviendas'].transform(lambda x: (x-x.mean())/x.std(ddof=0) if x.std(ddof=0)>0 else 0.0)
    s['viviendas_minmax'] = s.groupby('municipio')['viviendas'].transform(lambda x: (x-x.min())/(x.max()-x.min()) if x.max()>x.min() else 0.0)
    s['banda_viviendas'] = pd.cut(s['viviendas'], bins=[-0.01,0,10,50,np.inf],labels=['cero','1-10','11-50','mas_de_50'])
    s['nivel_geografico'] = 'municipal'
    s['anio_trimestre'] = s['año'].astype(str) + 'T' + s['trimestre'].astype(str)
    # IQR sólo como indicador de revisión; no se eliminan valores reales por ser extremos.
    q1,q3=s['viviendas'].quantile([.25,.75]); iqr=q3-q1
    s['atipico_iqr_global']=(s['viviendas']<q1-1.5*iqr)|(s['viviendas']>q3+1.5*iqr)
    DEST.mkdir(parents=True,exist_ok=True)
    s.to_parquet(DEST/'variables_analiticas_sniiv.parquet',index=False)
    pd.DataFrame(resultados).to_csv(DEST/'diagnostico_ampliado.csv',index=False,encoding='utf-8-sig')
    pd.DataFrame(pronosticos).to_csv(DEST/'pronosticos_exploratorios.csv',index=False,encoding='utf-8-sig')
    reporte={'sniiv_faltantes':{k:int(v) for k,v in registros.isna().sum().items()},'shf_colima_faltantes':{k:int(v) for k,v in datos.isna().sum().items()},'sniiv_atipicos_iqr_global':int(s['atipico_iqr_global'].sum()),'politica':'Sin imputación: no se observan nulos SNIIV y Municipio nulo SHF indica agregado estatal. Atípicos se señalan, no se borran.','reduccion':'Se conserva un subconjunto analítico de columnas para pronóstico municipal SHF y agregados trimestrales SNIIV.'}
    (DEST/'diagnostico_preprocesamiento.json').write_text(json.dumps(reporte,ensure_ascii=False,indent=2),encoding='utf-8')
    print(pd.DataFrame(resultados).to_string(index=False))
    print('Pronósticos exploratorios:',len(pronosticos),'filas; bandas NO calibradas')
    return reporte

if __name__ == '__main__':
    run()
