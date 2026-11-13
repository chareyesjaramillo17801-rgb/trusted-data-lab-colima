"""Ejecutar con python -m pipeline.ejecutar desde la raíz del repositorio."""
import json
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
from pipeline.limpieza import normalizar_columnas_texto
from pipeline.validacion import MESES, validar_sniiv, validar_shf

ROOT=Path(__file__).resolve().parents[1]

def guardar(df,ruta):
 ruta.parent.mkdir(parents=True,exist_ok=True)
 df.to_parquet(ruta,index=False)

def principal():
 bronce=ROOT/'data/bronce'
 archivos=sorted(p for p in (bronce/'sniiv_registro').glob('registro_*.json') if not p.name.endswith('.metadata.json'))
 if not archivos: raise FileNotFoundError('Sin capturas JSON SNIIV')
 shfs=sorted((bronce/'shf').glob('*.xlsx'))
 if not shfs: raise FileNotFoundError('Sin Excel SHF')
 origen_sniiv=archivos[-1]; origen_shf=shfs[-1]
 raw=json.loads(origen_sniiv.read_text(encoding='utf-8'))
 if not isinstance(raw,list): raise ValueError('SNIIV no es lista')
 sniiv=normalizar_columnas_texto(pd.DataFrame(raw),['mes','estado','municipio','segmento','clave_municipio','clave_estado'])
 sniiv['mes']=sniiv['mes'].astype('string').str.lower()
 sniiv['clave_estado']=sniiv['clave_estado'].astype('string').str.zfill(2)
 sniiv['clave_municipio']=sniiv['clave_municipio'].astype('string').str.zfill(3)
 sv,sr=validar_sniiv(sniiv)
 shf=pd.read_excel(origen_shf)
 shf=normalizar_columnas_texto(shf,['Estado','Municipio','Global'])
 # Solo Colima; el resto del archivo SHF es contexto nacional, no defectos.
 shf=shf.loc[shf['Estado'].eq('Colima').fillna(False)].copy().reset_index(drop=True)
 hv,hr=validar_shf(shf)
 if sv.empty or hv.empty: raise RuntimeError('Puerta de calidad: una fuente quedó sin datos válidos')
 sv['mes_numero']=sv['mes'].map(MESES).astype(int)
 sv['trimestre']=((sv['mes_numero']-1)//3+1).astype(int)
 sv['fecha']=pd.to_datetime(dict(year=sv['año'],month=sv['mes_numero'],day=1))
 hv['nivel_geografico']=np.where(hv['Municipio'].isna(),'estatal','municipal')
 hv['fecha']=pd.PeriodIndex.from_fields(year=hv['Año'],quarter=hv['Trimestre'],freq='Q').to_timestamp()
 guardar(sv,ROOT/'data/plata/sniiv.parquet')
 guardar(hv,ROOT/'data/plata/shf_colima.parquet')
 guardar(sr,ROOT/'data/cuarentena/sniiv.parquet')
 guardar(hr,ROOT/'data/cuarentena/shf_colima.parquet')
 # Mantener granulares separados; unir únicamente agregados trimestrales municipales.
 s_ag=sv.groupby(['municipio','año','trimestre'],as_index=False).agg(viviendas=('viviendas','sum'))
 h_m=hv.loc[hv['nivel_geografico'].eq('municipal'),['Municipio','Año','Trimestre','Indice']].rename(columns={'Municipio':'municipio','Año':'año','Trimestre':'trimestre','Indice':'indice_shf'})
 comparacion=s_ag.merge(h_m,on=['municipio','año','trimestre'],how='inner',validate='one_to_one')
 guardar(s_ag,ROOT/'data/oro/registros_trimestrales.parquet')
 guardar(hv,ROOT/'data/oro/indice_shf_colima.parquet')
 guardar(comparacion,ROOT/'data/oro/comparacion_municipal.parquet')
 reporte={'ejecutado_utc':datetime.now(timezone.utc).isoformat(),'origen_sniiv':str(origen_sniiv.relative_to(ROOT)),'origen_shf':str(origen_shf.relative_to(ROOT)),'sniiv_entrada':len(sniiv),'sniiv_validos':len(sv),'sniiv_rechazados':len(sr),'shf_colima_entrada':len(shf),'shf_validos':len(hv),'shf_rechazados':len(hr),'oro_comparaciones':len(comparacion),'nota':'No se imputan nulos estructurales ni se mezclan granularidades.'}
 (ROOT/'data/oro/reporte_calidad.json').write_text(json.dumps(reporte,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(reporte,ensure_ascii=False,indent=2))
 return reporte

if __name__=='__main__': principal()
