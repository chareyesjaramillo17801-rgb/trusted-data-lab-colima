import pandas as pd
from pipeline.limpieza import normalizar_texto
from pipeline.validacion import validar_sniiv, validar_shf

def ejemplo():
 return pd.DataFrame([{'año':2025,'mes':'enero','estado':'Colima','municipio':'Colima','segmento':'Popular','viviendas':3,'clave_municipio':'002','clave_estado':'06'}])

def test_normalizar():
 assert normalizar_texto(' Villa   de  Álvarez ')=='Villa de Álvarez'

def test_sniiv_valido():
 a,b=validar_sniiv(ejemplo()); assert len(a)==1 and b.empty

def test_sniiv_cuarentena():
 df=ejemplo(); df.loc[0,'viviendas']=-5
 a,b=validar_sniiv(df)
 assert a.empty and 'viviendas inválidas' in b.iloc[0]['motivo_rechazo']

def test_sniiv_tipo_invalido_a_cuarentena():
 df=ejemplo(); df['viviendas']=df['viviendas'].astype(object);df.loc[0,'viviendas']='invalido'
 a,b=validar_sniiv(df);assert a.empty and len(b)==1

def test_shf_nulo_estatal_no_es_defecto():
 df=pd.DataFrame([{'Consecutivo':1,'Global':pd.NA,'Estado':'Colima','Municipio':pd.NA,'Trimestre':1,'Año':2025,'Indice':180.0}])
 a,b=validar_shf(df); assert len(a)==1 and b.empty
