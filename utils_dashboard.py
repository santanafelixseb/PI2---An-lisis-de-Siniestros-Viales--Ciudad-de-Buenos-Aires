"""Funciones de utilidad en la aplicacion Streamlit
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# String invisible que crea espacios en blanco
STR_INVISIBLE = '‎'

# Paleta de colores
C_VERDE = '#139F39'
C_ROJO = '#F33221'


def md_write_at_size(input_string: str, font_size: int) -> None:
    """Rinde formato al string de entrada como markdown,
    con el tamaño de fuente especificado.
    """
    # Escapa cualquier carácter especial en la cadena de entrada
    escaped_string = input_string.replace("#", "\\#").replace("-", "\\-")
    
    # Crea la cadena de markdown formateada
    formatted_string = f"<span style='font-size: {font_size}px;'>{escaped_string}</span>"
    
    # Muestra el markdown formateado utilizando Streamlit
    st.markdown(formatted_string, unsafe_allow_html=True)


def get_md_color_kpi(valor_1: float, valor_2: float) -> str:
    """Devuelve un string con el color a utilizar para texto markdown, basado en
    las variables de entrada. Para uso en la representacion visual de los valores KPI.
    """
    return C_VERDE if valor_1 < valor_2 else C_ROJO


@st.cache_data
def cargar_df_homicidios() -> pd.DataFrame:
    """Carga y devuelve el dataframe 'df_homicidios'.
    """
    return pd.read_pickle('data/df_homicidios.pkl')


@st.cache_data
def cargar_datos_kpi() -> tuple[pd.DataFrame]:
    """Carga todo DataFrame relacionados a los KPI, y 
    devuelve un tuple de estos DataFrames.
    """
    df_kpi1_tasa = pd.read_pickle('data/df_kpi1_tasa.pkl')
    df_kpi2_moto = pd.read_pickle('data/df_kpi2_moto.pkl')
    df_kpi3_peaton = pd.read_pickle('data/df_kpi3_peaton.pkl')

    return df_kpi1_tasa, df_kpi2_moto, df_kpi3_peaton


def extraer_data_kpi(df: pd.DataFrame) -> tuple[float]:
    """Devuelve un tuple de valores extraidos del DataFrame de entrada,
    de datos relacionados al KPI. 
    """
    porcent_kpi = df['cambio_porcentual_KPI'].iat[-1]
    nominal_kpi = df['cambio_nominal_KPI'].iat[-1]
    meta_kpi = df['meta_KPI'].iat[-1]

    return porcent_kpi, nominal_kpi, meta_kpi


def numero_a_str_con_signo(numero: float) -> str:
    """Devuele un string de 'numero', con su respectivo
    signo de positivo/negativo ("+", "-").
    """
    return f'+{str(numero)}' if numero > 0 else str(numero)


@st.cache_data
def crear_graph_kpi_gauge(gauge_val: float, limite_val: float) -> go.Figure:
    """Devuele un grafo tipo "gauge", marcando un valor igual a 'gauge_val',
    y una linea delimitador, con el valor 'limite_val'.
    """
    LIM_FRACCION = 0.01  # ajusta el valor proporcional de 'lim_min' y 'lim_max'
    color_kpi = get_md_color_kpi(gauge_val, limite_val)
    # Definir paleta de colores
    #C_IZQ, C_DER, C_MID, C_KPI = '#2474B4', '#10346C', 'white', 'white' 
    C_IZQ, C_DER, C_MID, C_KPI = '#5494FC', '#0C3CFB', 'white', 'white' 
    
    rango = 1.5 * max(abs(gauge_val), abs(limite_val))
    lim_min = limite_val - (rango * LIM_FRACCION)
    lim_max = limite_val + (rango * LIM_FRACCION)
    
    # Crear grafica tipo "gauge+number"
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=gauge_val,
        number={'suffix':"%"},
        domain={'x':[0, 1], 'y':[0, 1]},
        gauge={
            'axis':{'range':[-rango, rango]},
            'bar':{'color':"rgba(0, 0, 0, 0)"},
            'steps':[
                {'range': [-rango, lim_min], 'color':C_IZQ},
                {'range': [lim_min, lim_max], 'color':C_MID},
                #{'range': [lim_max, 0], 'color':C_IZQ},
                {'range': [lim_max, rango], 'color':C_DER}
            ],
            'threshold' : {
                'line': {'color':C_KPI, 'width':6},
                'thickness': 0.65,
                'value': gauge_val
            }
        }
    ))
    # Configurar layout y color de texto
    fig.update_layout(
        autosize=True,
        width=180,
        height=180,
        margin={'l':20, 'r':20, 'b':0, 't':0, 'pad':0},
        font={'color':color_kpi, 'family':'Helvetica'},
        legend_font={'color':'white', 'family':'Helvetica'},
    )
    return fig


@st.cache_data
def crear_graph_kpi_linea(df: pd.DataFrame, col_y: str, title='') -> go.Figure:
    """Devuele un grafo tipo linea.
    """
    # Extraer valor de meta, para linea horizontal
    linea_meta = df['meta_KPI'].iat[0]

    # Crear grafo de linea
    fig = px.line(df, x=df.index, y=col_y)
    fig.add_hline(
        y=linea_meta,
        line_dash="dash", 
        line_color=C_VERDE, 
        annotation_text=f"Meta: {int(linea_meta)}%",
        annotation_position="right"
    )
    fig.update_layout(
        xaxis_title=title,
        yaxis_title=f"KPI {STR_INVISIBLE} (menos es mejor)",
        template="plotly_dark",  # Dark theme
        width=180,
        height=250,
        margin={'l':0, 'r':80, 'b':0, 't':0, 'pad':1},
        yaxis={'side':'left'},#{'autorange':'reversed', 'side':'left'},
        xaxis_tickangle=-60
    )
    return fig


def rendir_data_kpi(porcent_kpi: float, nominal_kpi: float, meta_kpi: float, texto='', subtexto='') -> None:
    """Rinde el texto, las metricas y otros objectos graficos relacionados a los KPI.
    """
    # Cambiar tipos de data, en base al KPI a rendir
    nominal_kpi = float(nominal_kpi) if texto=='Tasa de Homicidios' else int(nominal_kpi)
    # Crear columnas
    with st.columns((1,10))[1]:
        st.subheader(texto)
        st.markdown(subtexto)
    _, col1, col2, _ = st.columns((2,4,12,2))
    with col1:
        st.markdown(STR_INVISIBLE)
        st.metric('variación', '', delta=nominal_kpi, delta_color="inverse", label_visibility="visible")
    with col2:
        st.plotly_chart(crear_graph_kpi_gauge(porcent_kpi, meta_kpi), use_container_width=True)
    