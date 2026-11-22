"""Tablero E1. Consume exclusivamente productos locales generados por el pipeline."""
import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title='Observatorio inmobiliario · Colima', page_icon='🏠', layout='wide')

ROOT = Path(__file__).resolve().parents[1]
ORO = ROOT / 'data' / 'oro'


if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def preparar_datos():
    archivos_necesarios = [
        ORO / "reporte_calidad.json",
        ORO / "indice_shf_colima.parquet",
        ORO / "registros_trimestrales.parquet",
        ORO / "comparacion_modelos.csv",
        ORO / "pronosticos_exploratorios.csv",
        ORO / "diagnostico_ampliado.csv",
    ]


    archivos_completos = all(
        archivo.exists() for archivo in archivos_necesarios
    )

    columnas_linaje = {
        "ids_bronce_entrenamiento",
        "ids_bronce_prueba",
        "origen_bronce",
        "sha256_bronce",
        "fecha_ingesta_utc",
    }

    archivos_analiticos = [
        ORO / "comparacion_modelos.csv",
        ORO / "pronosticos_exploratorios.csv",
        ORO / "diagnostico_ampliado.csv",
    ]

    linaje_completo = archivos_completos

    if archivos_completos:
        for archivo in archivos_analiticos:
            columnas = set(pd.read_csv(archivo, nrows=0).columns)
            if not columnas_linaje.issubset(columnas):
                linaje_completo = False
                break

    if archivos_completos and linaje_completo:
        return

    from pipeline.ejecutar import principal
    from pipeline.ejecutar_analisis import principal as ejecutar_analisis

    with st.spinner("Preparando datos del observatorio..."):
        principal()
        ejecutar_analisis()

preparar_datos()

st.title('🏠 Observatorio inmobiliario de Colima')
st.caption('TRUSTED DATA LAB · E1 · Datos públicos SNIIV y SHF · Resultados exploratorios, no avalúos ni precios de renta')

@st.cache_data(show_spinner=False)
def csv(name):
    p=ORO/name
    return pd.read_csv(p) if p.exists() else None

@st.cache_data(show_spinner=False)
def parquet(name):
    p=ORO/name
    return pd.read_parquet(p) if p.exists() else None

@st.cache_data(show_spinner=False)
def js(name):
    p=ORO/name
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None

quality=js('reporte_calidad.json')
models=csv('comparacion_modelos.csv')
forecast=csv('pronosticos_exploratorios.csv')
diagnostics=csv('diagnostico_ampliado.csv')
series=parquet('indice_shf_colima.parquet')
registrations=parquet('registros_trimestrales.parquet')

if quality is None:
    st.error('Faltan productos Oro. Desde la raíz del repositorio ejecuta: python -m pipeline.ejecutar; python -m pipeline.estadistica; python -m pipeline.analisis_e1')
    st.stop()

st.subheader('Calidad de datos')
cols=st.columns(4)
for col, label, key in zip(cols,['SNIIV válidos','SHF válidos','SNIIV rechazados','SHF rechazados'],['sniiv_validos','shf_validos','sniiv_rechazados','shf_rechazados']):
    col.metric(label, quality.get(key,'No informado'))
with st.expander('Reporte de calidad completo'):
    st.json(quality)

st.subheader('Índice SHF: serie histórica')
st.info('SHF es un índice de precios de vivienda, no un precio de compraventa ni de renta. Los niveles geográficos se conservan separados.')
if series is not None and not series.empty:
    st.dataframe(series.head(30), width='stretch')
    columns = {str(c).strip().casefold(): c for c in series.columns}
    value = next((columns[k] for k in ('índice', 'indice', 'indice_shf') if k in columns), None)
    year_col = columns.get('año', columns.get('anio'))
    quarter_col = columns.get('trimestre')
    muni_col = columns.get('municipio')
    level_col = columns.get('nivel_geografico')

    if value is None or year_col is None or quarter_col is None:
        st.warning('No se reconocieron las columnas de índice, año y trimestre para graficar.')
    else:
        frame = series.copy()
        if level_col is not None:
            frame = frame[frame[level_col].astype(str).str.casefold() == 'municipal']
        if muni_col is not None:
            options = sorted(frame[muni_col].dropna().astype(str).unique())
            if options:
                chosen = st.selectbox('Municipio', options)
                frame = frame[frame[muni_col].astype(str) == chosen]
        frame['_year'] = pd.to_numeric(frame[year_col], errors='coerce')
        frame['_quarter'] = pd.to_numeric(frame[quarter_col], errors='coerce')
        frame['_index'] = pd.to_numeric(frame[value], errors='coerce')
        frame = frame.dropna(subset=['_year', '_quarter', '_index'])
        frame = frame[frame['_quarter'].between(1, 4)]
        frame = frame.sort_values(['_year', '_quarter'])
        if frame.duplicated(['_year', '_quarter']).any():
            st.error('Hay más de un registro por trimestre para este municipio. Se omite la gráfica para evitar mezclar series.')
        elif frame.empty:
            st.warning('No hay datos trimestrales válidos para graficar.')
        else:
            frame['fecha_grafica'] = pd.to_datetime(
                {'year': frame['_year'].astype(int),
                 'month': (frame['_quarter'].astype(int) - 1) * 3 + 1,
                 'day': 1}
            )
            chart_data = frame.set_index('fecha_grafica')['_index'].rename('Índice SHF')
            st.line_chart(chart_data, x_label='Trimestre', y_label='Índice SHF')
else:
    st.warning('No se encontró indice_shf_colima.parquet.')

st.subheader('Comparación de modelos con datos de prueba')
if models is not None and not models.empty:
    st.dataframe(models, width='stretch', hide_index=True)
    required={'municipio','modelo','mae'}
    if required.issubset(models.columns):
        valid=models.dropna(subset=['mae']).copy()
        valid['mae']=pd.to_numeric(valid['mae'],errors='coerce')
        valid=valid.dropna(subset=['mae'])
        if not valid.empty:
            best=valid.loc[valid.groupby('municipio')['mae'].idxmin(),['municipio','modelo','mae']]
            st.markdown('**Menor MAE observado por municipio**')
            st.dataframe(best,width='stretch',hide_index=True)
else:
    st.warning('Ejecuta python -m pipeline.estadistica para generar la comparación.')

st.subheader('Pronósticos exploratorios')
if forecast is not None and not forecast.empty:
    st.dataframe(forecast,width='stretch',hide_index=True)
    st.warning('Las bandas dependen del modelo: ARIMA usa intervalos paramétricos sujetos a sus supuestos; Holt usa bandas empíricas de backtesting. No se ha demostrado cobertura real del 95%, y Holt en Villa de Álvarez presenta autocorrelación residual.')
else:
    st.warning('Ejecuta python -m pipeline.analisis_e1 para generar los pronósticos.')

st.subheader('Diagnósticos y limitaciones')
if diagnostics is not None and not diagnostics.empty:
    st.dataframe(diagnostics,width='stretch',hide_index=True)
st.markdown('''**Interpretación responsable.** Un valor p alto en ADF no permite afirmar estacionariedad. Un valor p bajo en Ljung–Box sugiere autocorrelación residual; el modelo debe revisarse antes de utilizarlo en decisiones. Los datos SNIIV mensuales y SHF trimestrales no deben mezclarse sin agregación temporal explícita.''')

st.subheader('Registros SNIIV agregados a trimestre')
if registrations is not None and not registrations.empty:
    st.dataframe(registrations.head(100),width='stretch',hide_index=True)
else:
    st.caption('No se encontró el producto registros_trimestrales.parquet.')

# --- E2: mapa municipal INEGI con seleccion mediante clic ---
st.subheader('Mapa interactivo de los municipios de Colima · E2')
st.caption('Límites oficiales: INEGI. Indicadores históricos: SNIIV y SHF; no son precios de renta.')
map_path = ORO / 'municipios_colima.geojson'
if not map_path.exists():
    st.warning('No se encontró municipios_colima.geojson. Ejecuta: python -m pipeline.geoespacial_e2')
else:
    import folium
    from shapely.geometry import Point, shape
    from streamlit_folium import st_folium

    geo = json.loads(map_path.read_text(encoding='utf-8'))
    features = [f for f in geo.get('features', []) if f.get('geometry')]
    if not features:
        st.warning('El GeoJSON no contiene geometrías municipales.')
    else:
        st.write(f'Municipios con geometría oficial: **{len(features)}**')
        mapa = folium.Map(location=[19.15, -103.9], zoom_start=9, tiles="OpenStreetMap")
        folium.GeoJson(
            geo,
            name='Municipios de Colima (INEGI)',
            style_function=lambda feature: {
                'fillColor': '#2878a8', 'color': '#124a73',
                'weight': 2, 'fillOpacity': 0.24,
            },
            highlight_function=lambda feature: {
                'fillColor': '#f6bb42', 'color': '#a85a00',
                'weight': 3, 'fillOpacity': 0.45,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['municipio_inegi', 'cvegeo'],
                aliases=['Municipio:', 'Clave INEGI:'],
                sticky=True,
            ),
        ).add_to(mapa)
        folium.LayerControl().add_to(mapa)
        evento = st_folium(
            mapa, height=490, width=None,
            key='mapa_folium_e2',
            returned_objects=['last_object_clicked'],
        )
        st.caption('Haz clic dentro de un municipio para consultar sus indicadores. Usa + y − para acercarte o alejarte.')

        clic = (evento or {}).get('last_object_clicked')
        if clic and clic.get('lat') is not None and clic.get('lng') is not None:
            punto = Point(float(clic['lng']), float(clic['lat']))
            municipio_clic = next(
                (f.get('properties', {}).get('municipio_inegi')
                 for f in features if shape(f['geometry']).covers(punto)),
                None,
            )
            if municipio_clic:
                st.session_state['municipio_e2_clic'] = municipio_clic
            else:
                st.info('El punto seleccionado está fuera de los límites municipales cargados.')

        seleccionado = st.session_state.get('municipio_e2_clic')
        if not seleccionado:
            st.info('Selecciona un municipio haciendo clic en el mapa para ver sus indicadores.')
        else:
            st.markdown(f'**Municipio seleccionado: {seleccionado}**')
            if registrations is not None and not registrations.empty and {'municipio', 'viviendas'}.issubset(registrations.columns):
                subconjunto = registrations[
                    registrations['municipio'].astype(str).str.strip().str.casefold()
                    == seleccionado.strip().casefold()
                ]
                if subconjunto.empty:
                    st.info(f'No hay registros SNIIV disponibles para {seleccionado}.')
                else:
                    total = pd.to_numeric(subconjunto['viviendas'], errors='coerce').sum()
                    st.metric('Viviendas registradas SNIIV (suma histórica)', f'{total:,.0f}')
                    st.caption('No representa inventario de viviendas disponibles ni precios de renta.')
            else:
                st.warning('No está disponible el producto trimestral SNIIV.')

            if series is not None and not series.empty and 'Municipio' in series.columns:
                shf_m = series[
                    series['Municipio'].astype(str).str.strip().str.casefold()
                    == seleccionado.strip().casefold()
                ]
                if shf_m.empty:
                    st.info(f'No hay índice SHF municipal disponible para {seleccionado}.')
                else:
                    st.metric('Registros trimestrales de índice SHF', len(shf_m))
                    st.caption('El índice SHF no es un precio monetario.')
            else:
                st.warning('No está disponible el producto SHF.')

st.caption('Fuente: productos generados localmente por el pipeline del repositorio. Los archivos Oro se regeneran antes de abrir el tablero.')
