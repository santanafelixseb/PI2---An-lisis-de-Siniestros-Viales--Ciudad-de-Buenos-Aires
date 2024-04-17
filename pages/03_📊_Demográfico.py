import streamlit as st
import utils_dashboard as ud
import utils_dashb_graphs as udg


# Ajustes de pagina
st.set_page_config(
    page_title='📊 Demografía - Siniestros Viales CABA',
    layout='wide',
    initial_sidebar_state='auto'
)

# Cargar dataframe
df = ud.cargar_df_homicidios()


# Crear seleccion de Sexo
filtro_sexo = st.sidebar.multiselect(
    'Seleccione Sexo',
    ('MASCULINO', 'FEMENINO')
)

df_filtro_sexo = df[df['SEXO'].isin(filtro_sexo)]


# Crear columnas, primera fila
col1, col2, col3, _ = st.columns((3,3,6,1))
# Definimos tamano de Pie Chart y las columna
width_pie = 280
height_pie = 320
with col1:
    #st.markdown(ud.STR_INVISIBLE)
    st.plotly_chart(udg.crear_dem_graphpie_sexo(df, width=width_pie, height=height_pie), use_container_width=True)
with col2:
    #st.markdown(ud.STR_INVISIBLE)
    st.plotly_chart(udg.crear_dem_graphpie_edad(df_filtro_sexo, width=width_pie, height=height_pie), use_container_width=True)
with col3:
    st.plotly_chart(udg.crear_dem_histograma_edad(df_filtro_sexo, width=550, height=350), use_container_width=False)



# Columnas para graficas
col1, col2, col3, _ = st.columns((4,6,6,1))
# Asignar tamaño a graficas
width_g = 500
height_g = 400
with col1:
    st.plotly_chart(udg.crear_dem_graphpie_edad(df_filtro_sexo, width=width_pie, height=height_pie), use_container_width=True)
with col2:
    st.plotly_chart(udg.crear_dem_graphstack_clas_edad(df_filtro_sexo, width=width_g, height=height_g), use_container_width=True)
with col3:
    st.plotly_chart(udg.crear_dem_graphstack_acusado_edad(df_filtro_sexo, width=width_g, height=height_g), use_container_width=True)