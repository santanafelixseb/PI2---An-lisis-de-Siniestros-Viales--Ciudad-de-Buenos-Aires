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
    f'Seleccion {ud.STR_INVISIBLE}{ud.STR_INVISIBLE} Sexo',
    ('MASCULINO', 'FEMENINO')
)
# Si no hay seleccion en 'filtro_sexo', agreaga todos
if not filtro_sexo:
    filtro_sexo.append('MASCULINO')
    filtro_sexo.append('FEMENINO')


# Crear seleccion de Grupo Etario
filtro_edad = st.sidebar.multiselect(
    f'Seleccione {ud.STR_INVISIBLE}{ud.STR_INVISIBLE} Grupo Etario',
    ('<20', '21-40', '41-60', '61-80', '81+')
)
# Si no hay seleccion en 'filtro_sexo', agreaga todos
if not filtro_edad:
    filtro_edad.append('<20')
    filtro_edad.append('21-40')
    filtro_edad.append('41-60')
    filtro_edad.append('61-80')
    filtro_edad.append('81+')


# Filtramos la data por 'filtro_sexo'
df_filtros = df[df['SEXO'].isin(filtro_sexo) & df['EDAD_GRUPO'].isin(filtro_edad)]


# Crear columnas, primera fila
col1, col2, _, col4, _ = st.columns((3,3,0.3,5,2))
# Definimos tamano de Pie Chart y las columna
width_pie = 280
height_pie = 320
with col1:
    #st.markdown(ud.STR_INVISIBLE)
    st.plotly_chart(udg.crear_dem_graphpie_sexo(df, width=width_pie, height=height_pie), use_container_width=True)
with col2:
    #st.markdown(ud.STR_INVISIBLE)
    st.plotly_chart(udg.crear_dem_graphpie_edad(df_filtros, width=width_pie, height=height_pie), use_container_width=True)
with col4:
    st.plotly_chart(udg.crear_dem_histograma_edad(df_filtros, width=550, height=350), use_container_width=False)

# Columnas para graficas
col1, col2, col3, _ = st.columns((4,6,6,1))
# Asignar tamaño a graficas
width_g = 500
height_g = 400
with col1:
    st.plotly_chart(udg.crear_dem_graphpie_Top_4_Vict(df_filtros, width=width_pie, height=height_pie), use_container_width=True)
with col2:
    st.plotly_chart(udg.crear_dem_graphstack_clas_edad(df_filtros, width=width_g, height=height_g), use_container_width=True)
with col3:
    st.plotly_chart(udg.crear_dem_graphstack_acusado_edad(df_filtros, width=width_g, height=height_g), use_container_width=True)
