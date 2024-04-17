import streamlit as st
import utils_dashboard as ud


# Ajustes de pagina
st.set_page_config(
    page_title='Portal - Siniestros Viales CABA',
    layout='wide',
    initial_sidebar_state='auto'
)
with st.columns((1,10))[1]:
    st.markdown(ud.STR_INVISIBLE)
    st.markdown(ud.STR_INVISIBLE)
    
    st.subheader("Bienvenidos al data-driven Dashboard de")
    st.subheader("Sientros Viales - Ciudad de Buenos Aires")

    st.markdown(ud.STR_INVISIBLE)

    with st.columns((1,200))[1]:
        st.markdown(f"{ud.STR_INVISIBLE} ▷ {ud.STR_INVISIBLE} \
                    Para iniciar, seleccione una página")
        
        st.page_link("pages/01_📈_KPIs.py", label="KPIs", icon="📈")
        st.page_link("pages/02_🕖_Datos_Temporales.py", label="Datos Temporales", icon="🕖")
        st.page_link("pages/03_📊_Demográfico.py", label="Demográfico", icon="📊")
        st.page_link("pages/04_🗺️_Lugar de Hecho.py", label="Lugar de Hecho", icon="🗺️")