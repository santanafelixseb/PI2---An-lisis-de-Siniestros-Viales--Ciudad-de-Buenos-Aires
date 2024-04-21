import streamlit as st
import utils_dashboard as ud
import utils_dashb_graphs as udg


# Ajustes de pagina
st.set_page_config(
    page_title='🕖 Datos Temporales - Siniestros Viales CABA',
    layout='wide',
    initial_sidebar_state='auto'
)

# Cargar dataframe
df = ud.cargar_df_homicidios()

# Sidebar con slider para año
seleccion_anio = st.sidebar.slider("Seleccione Año", 2016, 2021, (2016, 2021))

# Filtrar 'df' por 'seleccion_anio'
df_filtro_anio = df[(df['AAAA'] >= seleccion_anio[0]) & (df['AAAA'] <= seleccion_anio[1])]

# Sumar/contar cantidad de victimas y hechos
num_victimas = df_filtro_anio['N_VICTIMAS'].sum()
num_hechos = df_filtro_anio.shape[0]

# Columnas para metricas 
_, col2, _, col4, _ = st.columns((1,5,2,30,7))
with col2:
    pass  # Espacio en blanco
    st.markdown(ud.STR_INVISIBLE)  # insertar espacio invisible
    with st.container(border=True):
        st.markdown(f"{ud.STR_INVISIBLE} {seleccion_anio[0]} - {seleccion_anio[1]}")
        st.metric(f'{ud.STR_INVISIBLE} Victimas', num_victimas)
        st.metric(f'{ud.STR_INVISIBLE} Hechos', num_hechos)
with col4:
    st.plotly_chart(udg.crear_dt_histograma_fecha(df_filtro_anio, width=500, height=325), use_container_width=True)
    

# Columnas para graficas
col1, _, col3, _ = st.columns((5,0.3,5,2))
# Asignar tamaño a graficas
width_g = 500
height_g = 325
with col1:
    st.plotly_chart(udg.crear_dt_graphstack_clasificacion(df_filtro_anio, width=700, height=300), use_container_width=True)
    st.plotly_chart(udg.crear_dt_graphlinea_estacion(df_filtro_anio, width=width_g, height=height_g), use_container_width=True)
    st.plotly_chart(udg.crear_dt_graphlinea_semana(df_filtro_anio, width=width_g, height=height_g), use_container_width=True)
with col3:
    st.plotly_chart(udg.crear_dt_graphlinea_fecha(df_filtro_anio, width=width_g, height=height_g), use_container_width=True)
    st.plotly_chart(udg.crear_dt_graphlinea_mes(df_filtro_anio, width=width_g, height=height_g), use_container_width=True)
    st.plotly_chart(udg.crear_dt_graphlinea_franja(df_filtro_anio, width=width_g, height=height_g), use_container_width=True)
