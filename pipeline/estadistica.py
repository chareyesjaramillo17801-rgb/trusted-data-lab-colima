"""Diagnóstico de atípicos y comparación de modelos trimestrales SHF."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing, Holt, SimpleExpSmoothing
from statsmodels.tsa.stattools import acf, adfuller, pacf

ROOT = Path(__file__).resolve().parents[1]

def metricas(y, pred):
    y=np.asarray(y,dtype=float);pred=np.asarray(pred,dtype=float)
    return {'mae':float(np.mean(np.abs(y-pred))), 'rmse':float(np.sqrt(np.mean((y-pred)**2))), 'mape':float(np.mean(np.abs((y-pred)/y))*100)}

def analizar():
    shf=pd.read_parquet(ROOT/'data/plata/shf_colima.parquet')
    resultados=[]; diagnosticos=[]
    for municipio in ['Manzanillo','Villa de Álvarez']:
        datos=shf.loc[shf['Municipio'].eq(municipio)].sort_values(['Año','Trimestre'])
        serie=datos['Indice'].astype(float).reset_index(drop=True)
        if len(serie)<24: raise ValueError(f'Serie insuficiente: {municipio}')
        q1,q3=serie.quantile([.25,.75]); iqr=q3-q1
        n_atipicos=int(((serie<q1-1.5*iqr)|(serie>q3+1.5*iqr)).sum())
        train=serie.iloc[:-8]; test=serie.iloc[-8:]
        diagnosticos.append({'municipio':municipio,'observaciones':len(serie),'atipicos_iqr_nivel':n_atipicos,'adf_pvalor_nivel':float(adfuller(serie,autolag='AIC')[1]),'adf_pvalor_diferencia':float(adfuller(serie.diff().dropna(),autolag='AIC')[1]),'acf_lag1':float(acf(serie,nlags=1)[1]),'pacf_lag1':float(pacf(serie,nlags=1)[1])})
        modelos={
            'SES':lambda train=train, test=test: SimpleExpSmoothing(train,initialization_method='estimated').fit().forecast(len(test)),
            'Holt':lambda train=train, test=test: Holt(train,initialization_method='estimated').fit().forecast(len(test)),
            'Holt-Winters':lambda train=train, test=test: ExponentialSmoothing(train,trend='add',seasonal='add',seasonal_periods=4,initialization_method='estimated').fit().forecast(len(test)),
            'ARIMA(1,1,1)':lambda train=train, test=test: ARIMA(train,order=(1,1,1)).fit().forecast(len(test)),
        }
        for nombre,fn in modelos.items():
            try:
                pred=fn()
                resultados.append({'municipio':municipio,'modelo':nombre,'periodos_entrenamiento':len(train),'periodos_prueba':len(test),**metricas(test,pred),'error':''})
            except Exception as e:  # noqa: BLE001 - registrar fallo de cada modelo sin abortar los demás
                resultados.append({'municipio':municipio,'modelo':nombre,'error':str(e)})
    destino=ROOT/'data/oro'
    destino.mkdir(exist_ok=True,parents=True)
    pd.DataFrame(resultados).to_csv(destino/'comparacion_modelos.csv',index=False,encoding='utf-8-sig')
    (destino/'diagnostico_series.json').write_text(json.dumps(diagnosticos,ensure_ascii=False,indent=2),encoding='utf-8')
    print(pd.DataFrame(resultados).to_string(index=False))
    print('Diagnóstico:',json.dumps(diagnosticos,ensure_ascii=False,indent=2))

if __name__=='__main__': analizar()
