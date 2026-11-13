"""Puerta de calidad: validación por fila y esquemas Pandera sobre aceptados."""
import pandas as pd
import pandera.pandas as pa

MESES = {m: i for i, m in enumerate('enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre'.split(), 1)}
MUNICIPIOS = {'Armería':'001','Colima':'002','Comala':'003','Coquimatlán':'004','Cuauhtémoc':'005','Ixtlahuacán':'006','Manzanillo':'007','Minatitlán':'008','Tecomán':'009','Villa de Álvarez':'010'}
COLUMNAS_SNIIV = ['año','mes','estado','municipio','segmento','viviendas','clave_municipio','clave_estado']
COLUMNAS_SHF = ['Consecutivo','Global','Estado','Municipio','Trimestre','Año','Indice']
ESQUEMA_SNIIV = pa.DataFrameSchema({
 'año':pa.Column(int,pa.Check.in_range(2010,2100)),
 'mes':pa.Column(str,pa.Check.isin(list(MESES))),
 'estado':pa.Column(str,pa.Check.eq('Colima')),
 'municipio':pa.Column(str,pa.Check.isin(list(MUNICIPIOS))),
 'segmento':pa.Column(str),
 'viviendas':pa.Column(int,pa.Check.ge(0)),
 'clave_municipio':pa.Column(str),
 'clave_estado':pa.Column(str,pa.Check.eq('06'))},strict=False,coerce=False)
ESQUEMA_SHF = pa.DataFrameSchema({
 'Año':pa.Column(int,pa.Check.in_range(2005,2100)),
 'Trimestre':pa.Column(int,pa.Check.in_range(1,4)),
 'Indice':pa.Column(float,pa.Check.gt(0)),
 'Estado':pa.Column(str,nullable=True),
 'Municipio':pa.Column(str,nullable=True)},strict=False,coerce=False)

def _partir(df, razones):
 motivos = razones.map(lambda x: '; '.join(x))
 malos = motivos.ne('')
 validos = df.loc[~malos].copy()
 rechazados = df.loc[malos].copy()
 rechazados['motivo_rechazo'] = motivos.loc[malos]
 return validos, rechazados

def validar_sniiv(df):
 faltan=set(COLUMNAS_SNIIV)-set(df.columns)
 if faltan: raise ValueError('Esquema SNIIV incompleto: '+str(sorted(faltan)))
 razones=pd.Series([[] for _ in range(len(df))],index=df.index,dtype=object)
 vistos=set()
 for i,r in df.iterrows():
  x=razones.at[i]
  anio=pd.to_numeric(r['año'],errors='coerce'); viv=pd.to_numeric(r['viviendas'],errors='coerce')
  if pd.isna(anio) or anio!=int(anio) or not 2010<=anio<=2100: x.append('año inválido')
  if r['mes'] not in MESES: x.append('mes inválido')
  if r['estado']!='Colima': x.append('estado inválido')
  if r['municipio'] not in MUNICIPIOS: x.append('municipio desconocido')
  if pd.isna(r['segmento']) or not str(r['segmento']).strip(): x.append('segmento vacío')
  if pd.isna(viv) or viv!=int(viv) or viv<0: x.append('viviendas inválidas')
  if r['clave_estado']!='06': x.append('clave estatal inválida')
  if r['municipio'] in MUNICIPIOS and str(r['clave_municipio'])!=MUNICIPIOS[r['municipio']]: x.append('clave municipal incongruente')
  clave=tuple(str(r[c]) for c in ['año','mes','clave_municipio','segmento'])
  if clave in vistos: x.append('clave dimensional duplicada')
  vistos.add(clave)
 validos, rechazados=_partir(df,razones)
 if not validos.empty: ESQUEMA_SNIIV.validate(validos,lazy=True)
 return validos,rechazados

def validar_shf(df):
 faltan=set(COLUMNAS_SHF)-set(df.columns)
 if faltan: raise ValueError('Esquema SHF incompleto: '+str(sorted(faltan)))
 razones=pd.Series([[] for _ in range(len(df))],index=df.index,dtype=object)
 vistos=set()
 for i,r in df.iterrows():
  x=razones.at[i]; anio=pd.to_numeric(r['Año'],errors='coerce'); tri=pd.to_numeric(r['Trimestre'],errors='coerce'); indice=pd.to_numeric(r['Indice'],errors='coerce')
  if pd.isna(anio) or anio!=int(anio) or not 2005<=anio<=2100: x.append('año inválido')
  if pd.isna(tri) or tri!=int(tri) or not 1<=tri<=4: x.append('trimestre inválido')
  if pd.isna(indice) or indice<=0: x.append('índice inválido')
  if r['Estado']!='Colima': x.append('estado fuera del alcance')
  if pd.notna(r['Municipio']) and r['Municipio'] not in MUNICIPIOS: x.append('municipio desconocido')
  if pd.notna(r['Global']): x.append('categoría Global inesperada para nivel estatal/municipal')
  clave=(str(r['Año']),str(r['Trimestre']),str(r['Municipio']))
  if clave in vistos: x.append('clave dimensional duplicada')
  vistos.add(clave)
 validos,rechazados=_partir(df,razones)
 if not validos.empty: ESQUEMA_SHF.validate(validos,lazy=True)
 return validos,rechazados
