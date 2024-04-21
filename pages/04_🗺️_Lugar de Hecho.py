import streamlit as st
import utils_dashboard as ud
import utils_dashb_graphs as udg


# Ajustes de pagina
st.set_page_config(
    page_title='🌎 Lugar de Hecho - Siniestros Viales CABA',
    layout='wide',
    initial_sidebar_state='auto'
)

# Cargar dataframe
df = ud.cargar_df_homicidios()

# Crear columnas, primera fila
col1, _, col3, _ = st.columns((5,0.1,2,1))
# Definimos tamano de Pie Chart y las columna
width = 500
height = 350
with col1:
    #st.markdown(ud.STR_INVISIBLE)
    st.plotly_chart(udg.crear_lh_graphpareto_comuna(df, width=width, height=350), use_container_width=True)
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.plotly_chart(udg.crear_lh_graphstack_diasemana_calle(df, width=width, height=height), use_container_width=True)
    with subcol2:
        st.plotly_chart(udg.crear_lh_graphstack_franja_calle(df, width=width, height=height), use_container_width=True)
with col3:
    st.plotly_chart(udg.crear_lh_graphpie_tipocalle(df, width=width, height=280), use_container_width=True)
    st.plotly_chart(udg.crear_lh_graphpie_cruce(df, width=width, height=350), use_container_width=True)
