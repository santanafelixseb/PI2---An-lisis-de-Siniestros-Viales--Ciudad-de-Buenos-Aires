import streamlit as st
import utils_dashboard as ud


# Ajustes de pagina
st.set_page_config(
    page_title='📈 KPI - Siniestros Viales CABA',
    layout='wide',
    initial_sidebar_state='auto'
)

# Titulo de pagina
#st.subheader(f"KPI's de Siniestros Viales")

# Cargar data KPI's
df_kpi1_tasa, df_kpi2_moto, df_kpi3_peaton = ud.cargar_datos_kpi()

# Crear columnas donde se muestran los KPI
col1, col2, col3, _ = st.columns((4,4,4,1), gap='medium')
# Rendir la representacion grafica de lo KPI, en sus columnas respectivas
with col1:
    with st.container(border=True):  # un contenedor, con un borde ilustrado
        ud.rendir_data_kpi(*ud.extraer_data_kpi(df_kpi1_tasa),
                           texto='Tasa de Homicidios',
                           subtexto='Reducir un 10% la tasa de homicidios por semestre.'
        )
with col2:
    with st.container(border=True):  # un contenedor, con un borde ilustrado
        ud.rendir_data_kpi(*ud.extraer_data_kpi(df_kpi2_moto),
                           texto='Homicidios de Moto',
                           subtexto='Reducir un 7% muertes de motociclistas anualmente.'
        )
with col3:
    with st.container(border=True):  # un contenedor, con un borde ilustrado
        ud.rendir_data_kpi(*ud.extraer_data_kpi(df_kpi3_peaton),
                           texto='Homicidios de Peatón',
                           subtexto='Reducir un 7% muertes de peatones anualmente.'
        )


# Nueva linea de columna, con titulo "Tendencias Históricas"
st.markdown(ud.STR_INVISIBLE)  # insertar espacio invisible
st.subheader("Tendencias Históricas")

# Crear columnas donde se muestran los KPI
col1, col2, col3, _ = st.columns((4,4,4,1), gap='medium')
# Rendir la representacion grafica de lo KPI, en sus columnas respectivas
with col1:
    st.markdown(f'KPI {ud.STR_INVISIBLE} Tasa Homicidios')
    st.plotly_chart(ud.crear_graph_kpi_linea(df_kpi1_tasa, 'cambio_porcentual_KPI', title="Semestre"), use_container_width=True)
with col2:
    st.markdown(f'KPI {ud.STR_INVISIBLE} Homicidios Moto')
    st.plotly_chart(ud.crear_graph_kpi_linea(df_kpi2_moto, 'cambio_porcentual_KPI', title="Año"),use_container_width=True)
with col3:
    st.markdown(f'KPI {ud.STR_INVISIBLE} Homicidios Peatón')
    st.plotly_chart(ud.crear_graph_kpi_linea(df_kpi3_peaton, 'cambio_porcentual_KPI', title="Año"), use_container_width=True)
