"""Ejecutar con python -m pipeline.ejecutar desde la raíz del repositorio."""
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
import pandas as pd

from pipeline.limpieza import normalizar_columnas_texto
from pipeline.validacion import MESES, validar_shf, validar_sniiv

ROOT=Path(__file__).resolve().parents[1]

def guardar(df,ruta):
 ruta.parent.mkdir(parents=True,exist_ok=True)
 df.to_parquet(ruta,index=False)

def sha256_archivo(ruta):
 h=hashlib.sha256()
 with ruta.open('rb') as stream:
  for bloque in iter(lambda:stream.read(1024*1024),b''): h.update(bloque)
 return h.hexdigest()

def fecha_ingesta(ruta):
 """Fecha del lote: metadata de captura si existe; si no, fecha de archivo con advertencia."""
 meta=ruta.with_name(ruta.stem+'.metadata.json')
 if meta.exists():
  try:
   datos=json.loads(meta.read_text(encoding='utf-8'))
   for clave in ('captured_at_utc','ingested_at_utc','fecha_ingesta_utc'):
    if datos.get(clave): return str(datos[clave]), 'metadatos_captura'
  except (ValueError, OSError): pass
 return datetime.fromtimestamp(ruta.stat().st_mtime, tz=UTC).isoformat(), 'mtime_archivo_no_verificado'

def agregar_linaje(df, ruta, ids):
 fecha,metodo=fecha_ingesta(ruta)
 df=df.copy()
 df['origen_bronce']=str(ruta.relative_to(ROOT)).replace('\\','/')
 df['sha256_bronce']=sha256_archivo(ruta)
 df['fecha_ingesta_utc']=fecha
 df['metodo_fecha_ingesta']=metodo
 df['id_fila_bronce']=ids
 return df

def vinculos_agregacion(df, claves):
 """Conserva los IDs de todas las filas que contribuyeron a cada agregado."""
 return (df.groupby(claves,dropna=False)['id_fila_bronce']
         .agg(lambda x:json.dumps(sorted(x.astype(str).tolist()),ensure_ascii=False))
         .reset_index(name='ids_filas_bronce'))

def principal():
 bronce=ROOT/'data/bronce'
 archivos=sorted(p for p in (bronce/'sniiv_registro').glob('registro_*.json') if not p.name.endswith('.metadata.json'))
 if not archivos: raise FileNotFoundError('Sin capturas JSON SNIIV')
 shfs=sorted((bronce/'shf').glob('*.xlsx'))
 if not shfs: raise FileNotFoundError('Sin Excel SHF')
 origen_sniiv=archivos[-1]; origen_shf=shfs[-1]
 raw=json.loads(origen_sniiv.read_text(encoding='utf-8'))
 if not isinstance(raw,list): raise TypeError('SNIIV no es lista')
 sniiv=normalizar_columnas_texto(agregar_linaje(pd.DataFrame(raw),origen_sniiv,[f'sniiv:{i}' for i in range(len(raw))]),['mes','estado','municipio','segmento','clave_municipio','clave_estado'])
 sniiv['mes']=sniiv['mes'].astype('string').str.lower()
 sniiv['clave_estado']=sniiv['clave_estado'].astype('string').str.zfill(2)
 sniiv['clave_municipio']=sniiv['clave_municipio'].astype('string').str.zfill(3)
 sv,sr=validar_sniiv(sniiv)
 shf=pd.read_excel(origen_shf)
 shf=agregar_linaje(shf,origen_shf,[f'shf:excel_fila:{i+2}' for i in range(len(shf))])
 shf=normalizar_columnas_texto(shf,['Estado','Municipio','Global'])
 # Solo Colima; el resto del archivo SHF es contexto nacional, no defectos.
 shf=shf.loc[shf['Estado'].eq('Colima').fillna(False)].copy().reset_index(drop=True)
 hv,hr=validar_shf(shf)
 if sv.empty or hv.empty: raise RuntimeError('Puerta de calidad: una fuente quedó sin datos válidos')
 sv['mes_numero']=sv['mes'].map(MESES).astype(int)
 sv['trimestre']=((sv['mes_numero']-1)//3+1).astype(int)
 sv['fecha']=pd.to_datetime({'year': sv['año'], 'month': sv['mes_numero'], 'day': 1})
 hv['nivel_geografico']=np.where(hv['Municipio'].isna(),'estatal','municipal')
 hv['fecha']=pd.PeriodIndex.from_fields(year=hv['Año'],quarter=hv['Trimestre'],freq='Q').to_timestamp()
 guardar(sv,ROOT/'data/plata/sniiv.parquet')
 guardar(hv,ROOT/'data/plata/shf_colima.parquet')
 guardar(sr,ROOT/'data/cuarentena/sniiv.parquet')
 guardar(hr,ROOT/'data/cuarentena/shf_colima.parquet')
 # Mantener granulares separados; unir únicamente agregados trimestrales municipales.
 s_ag=sv.groupby(['municipio','año','trimestre'],as_index=False).agg(viviendas=('viviendas','sum'))
 vinculos=vinculos_agregacion(sv,['municipio','año','trimestre'])
 s_ag=s_ag.merge(vinculos,on=['municipio','año','trimestre'],validate='one_to_one')
 for columna in ['origen_bronce','sha256_bronce','fecha_ingesta_utc','metodo_fecha_ingesta']:
  s_ag[columna]=sv[columna].iloc[0]
 s_ag['id_registro_oro']=['sniiv_trimestre:'+str(i) for i in range(len(s_ag))]
 h_m=hv.loc[hv['nivel_geografico'].eq('municipal'),['Municipio','Año','Trimestre','Indice','id_fila_bronce','origen_bronce','sha256_bronce','fecha_ingesta_utc','metodo_fecha_ingesta']].rename(columns={'Municipio':'municipio','Año':'año','Trimestre':'trimestre','Indice':'indice_shf'})
 comparacion=s_ag.merge(h_m,on=['municipio','año','trimestre'],how='inner',validate='one_to_one',suffixes=('_sniiv','_shf'))
 comparacion['id_registro_oro']=['comparacion:'+str(i) for i in range(len(comparacion))]
 hv['id_registro_oro']=['shf:'+str(i) for i in range(len(hv))]
 guardar(s_ag,ROOT/'data/oro/registros_trimestrales.parquet')
 guardar(hv,ROOT/'data/oro/indice_shf_colima.parquet')
 guardar(comparacion,ROOT/'data/oro/comparacion_municipal.parquet')
 reporte={'ejecutado_utc':datetime.now(UTC).isoformat(),'origen_sniiv':str(origen_sniiv.relative_to(ROOT)),'origen_shf':str(origen_shf.relative_to(ROOT)),'sniiv_entrada':len(sniiv),'sniiv_validos':len(sv),'sniiv_rechazados':len(sr),'shf_colima_entrada':len(shf),'shf_validos':len(hv),'shf_rechazados':len(hr),'oro_comparaciones':len(comparacion),'linaje_e2':'por fila para SNIIV, SHF y comparacion; ver docs/E2/LINAJE.md','nota':'No se imputan nulos estructurales ni se mezclan granularidades.'}
 (ROOT/'data/oro/reporte_calidad.json').write_text(json.dumps(reporte,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(reporte,ensure_ascii=False,indent=2))
 return reporte

if __name__=='__main__': principal()
