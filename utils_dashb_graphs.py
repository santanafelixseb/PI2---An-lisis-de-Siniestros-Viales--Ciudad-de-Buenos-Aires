"""Funciones de creacion de graficas, para la aplicacion Streamlit
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



####  Funciones de 'Datos Temporales'  ####


def crear_dt_histograma_fecha(df_in, width=700, height=350):
    """Crea una grafica de barras de Histograma de Victimas.
    """
    # Instanciamos un nuevo dataframe
    df = pd.DataFrame()
    # Create a new column for date bins
    df['date_bin'] = pd.cut(df_in['FECHA_HORA'], bins=80)
    # Convertimos el formato de 'date_bin', para mostrar fechas como YYYY-MM
    df['date_bin'] = df['date_bin'].apply(lambda x: f'{x.left.strftime("%Y-%m")}')
    # Agrupamos por bins y contamos las filas
    df_grouped = df.groupby('date_bin').size().reset_index(name='count')
    # Crea la grafica de barra
    fig = px.bar(df_grouped, x='date_bin', y='count', labels={'date_bin':'Fecha', 'count':'Victimas'},
                title='Histograma Victimas',)
    fig.update_layout(autosize=False, width=width, height=height,
                      template='ggplot2')
    return fig


def crear_dt_graphlinea_fecha(df_in, width=700, height=350):
    """Crea una grafica de linea de Victimas por Fecha.
    """
    # Instanciamos un nuevo dataframe
    df = pd.DataFrame()
    # Create a new column for date bins
    df['date_bin'] = pd.cut(df_in['FECHA_HORA'], bins=24)
    # Convertimos el formato de 'date_bin', para mostrar fechas como YYYY-MM
    df['date_bin'] = df['date_bin'].apply(lambda x: f'{x.left.strftime("%Y-%m")}')
    # Agrupamos por bins y contamos las filas
    df_grouped = df.groupby('date_bin').size().reset_index(name='count')
    # Crea la grafica de linea
    fig = px.line(df_grouped, x='date_bin', y='count', labels={'date_bin':'Fecha', 'count':'Victimas'},
                title='Victimas por Fecha - Tendencias',)
    fig.update_layout(autosize=False, width=width, height=height,
                      template='plotly_dark')
    return fig


def crear_dt_graphlinea_franja(df_in, width=700, height=350):
    # Crea una grafica de victimas por hora
    # Agrupamos victimas por franja hora
    df_agrupado = df_in.groupby('Franja_Hora')['N_VICTIMAS'].sum().reset_index()
    fig = px.line(df_agrupado, x='Franja_Hora', y='N_VICTIMAS', title='Victimas por Franja Hora')
    # Adjutamos el tamano
    fig.update_layout(xaxis_title="Franja Hora", yaxis_title="Victimas",
                      autosize=False, width=width, height=height,
                      template='plotly_dark')
    return fig


def crear_dt_graphlinea_semana(df_in, width=700, height=350):
    # Crea una grafica de victimas por Dia de Semana
    # Agrupamos victimas por dia de semana
    df_agrupado = df_in.groupby('DIA_DE_SEMANA')['N_VICTIMAS'].sum().reset_index()
    fig = px.line(df_agrupado, x='DIA_DE_SEMANA', y='N_VICTIMAS', title='Victimas por Dia de Semana')
    # Adjutamos el tamano
    fig.update_layout(xaxis_title="Dia de Semana", yaxis_title="Victimas",
                      autosize=False, width=width, height=height,
                      template='plotly_dark')
    return fig


def crear_dt_graphlinea_mes(df_in, width=700, height=350):
    # Crea una grafica de victimas por mes
    # Agrupamos victimas por mes
    df_agrupado = df_in.groupby('MES')['N_VICTIMAS'].sum().reset_index()
    fig = px.line(df_agrupado, x='MES', y='N_VICTIMAS', title='Victimas por Mes')
    # Adjutamos el tamano
    fig.update_layout(xaxis_title="Mes", yaxis_title="Victimas",
                    autosize=False, width=width, height=height,
                    template='plotly_dark')
    return fig


def crear_dt_graphlinea_estacion(df_in, width=700, height=350):
    # Crea una grafica de victimas por estacion
    # Agrupamos victimas por Estaciones
    df_agrupado = df_in.groupby('Estaciones')[['N_VICTIMAS']].sum().reset_index()
    fig = px.line(df_agrupado, x='Estaciones', y='N_VICTIMAS', title='Victimas por Estación')
    # Adjutamos el tamano
    fig.update_layout(xaxis_title="Estación", yaxis_title="Victimas",
                    autosize=False, width=width, height=height,
                    template='plotly_dark')
    return fig


def crear_dt_graphstack_clasificacion(df_in, width=600, height=450):
    # Crea una grafica de victimas por Año
    df = df_in.copy()
    df['AAAA'] = df['AAAA'].astype(str)
    # Agrupamos por Año y Victima
    df_agrupado = df.groupby(['AAAA', 'VICTIMA']).size().unstack()
    # Crea una grafica de barras tipo stacked
    fig = go.Figure(data=[
        go.Bar(name=col, x=df_agrupado.index, y=df_agrupado[col]) for col in df_agrupado.columns
    ])
    # Configuramos el layout
    fig.update_layout(barmode='stack', xaxis_title='Año', yaxis_title='Victimas',
                    title='Victima por Año',
                    autosize=False, width=width, height=height,
                    margin={'l':0, 'r':0, 'b':0, 't':60, 'pad':0},
                    legend=dict(x=1, y=1),
                    legend_title='Victima',
                    template='plotly_dark'
    )
    return fig



####  Funciones de 'Demográfico'  ####


def crear_dem_graphpie_sexo(df_in, width=600, height=450):
    # Crea una grafica Pie-chart
    # Primero filtramos fuera los datos nulos
    df = df_in[df_in['SEXO'].notna()]
    # Crea la grafica
    fig = go.Figure(data=[go.Pie(labels=df['SEXO'],
                                values=df['N_VICTIMAS'],
                                rotation=180,
                                textposition='outside'
    )])
    # Configuramos el layout
    fig.update_layout(title='Proporción Victimas por Sexo',
                    autosize=False, width=width, height=height,
                    #margin={'l':20, 'r':0, 'b':0, 't':0, 'pad':0},
                    legend=dict(x=1, y=1),
                    legend_title='Sexo',
                    template='plotly_dark'
    )
    return fig


def crear_dem_graphpie_edad(df_in, width=600, height=450):
    # Crea una grafica Pie-chart
    fig = go.Figure(data=[go.Pie(labels=df_in['EDAD_GRUPO'],
        values=df_in['N_VICTIMAS'],
        rotation=90,
        textposition='outside'
    )])
    # Configuramos el layout
    fig.update_layout(title='Proporción Victimas por Grupo Etario',
        autosize=False, width=width, height=height,
        #margin={'l':0, 'r':60, 'b':0, 't':0, 'pad':0},
        legend=dict(x=1, y=1),
        legend_title='Grupo Etario',
        template='plotly_dark'
    )
    return fig


def crear_dem_graphpie_edad(df_in, width=600, height=450):
    # Crea una grafica Pie-chart
    # Filtramos por victimas con mayor frecuancia, para no sobrecargar la grafica
    victima_filtro = ['AUTO','BICICLETA','MOTO','PEATON']
    df = df_in[df_in['VICTIMA'].isin(victima_filtro)]
    # Crea la grafica
    fig = go.Figure(data=[go.Pie(labels=df['VICTIMA'],
                                values=df['N_VICTIMAS'],
                                rotation=90,
                                textposition='outside'
    )])
    # Configuramos el layout
    fig.update_layout(title='Proporción Top 4 Victimas',
                    autosize=False, width=width, height=height,
                    legend=dict(x=1, y=1),
                    legend_title='Victima',
                    template='plotly_dark'
    )
    return fig


def crear_dem_histograma_edad(df_in, width=600, height=450):
    # Crea un histograma de 'EDAD'
    fig = px.histogram(df_in, x='EDAD', nbins=50, title='Histograma de Edades')
    fig.update_layout(xaxis_title='Edad',
                    yaxis_title='Victimas',
                    autosize=False, width=width, height=height,
                    template='simple_white'
    )
    return fig


def crear_dem_graphstack_clas_edad(df_in, width=600, height=450):
    # Agrupamos por 'VICTIMA' y 'EDAD_GRUPO'
    df = df_in.copy()
    df_agrupado = df.groupby(['VICTIMA', 'EDAD_GRUPO']).size().unstack()
    # Sumamos las filas y aplicamos un sort
    df_agrupado['suma'] = df_agrupado.sum(axis=1)
    df_agrupado.sort_values('suma', ascending=False, inplace=True)
    df_agrupado.drop(columns='suma', inplace=True)
    # Crea una grafica de barras tipo stacked
    fig = go.Figure(data=[
        go.Bar(name=col, x=df_agrupado.index, y=df_agrupado[col]) for col in df_agrupado.columns
    ])
    # Configuramos el layout
    fig.update_layout(barmode='stack', xaxis_title='Tipo Victima', yaxis_title='Victimas',
                    title='Tipo de Victimas',
                    autosize=False, width=width, height=height,
                    legend=dict(x=1, y=1),
                    legend_title='Grupo Etario',
                    template='plotly_dark'
    )
    return fig


def crear_dem_graphstack_acusado_edad(df_in, width=600, height=450):
    # Agrupamos por 'ROL' y 'EDAD_GRUPO'
    df = df_in.copy()
    df_agrupado = df.groupby(['ACUSADO', 'EDAD_GRUPO']).size().unstack()
    # Sumamos las filas y aplicamos un sort
    df_agrupado['suma'] = df_agrupado.sum(axis=1)
    df_agrupado.sort_values('suma', ascending=False, inplace=True)
    df_agrupado.drop(columns='suma', inplace=True)
    # Crea una grafica de barras tipo stacked
    fig = go.Figure(data=[
        go.Bar(name=col, x=df_agrupado.index, y=df_agrupado[col]) for col in df_agrupado.columns
    ])
    # Configuramos el layout
    fig.update_layout(barmode='stack', xaxis_title='Acusado', yaxis_title='Victimas',
                    title='Victimas por Acusado',
                    autosize=False, width=width, height=height,
                    legend_title='Grupo Etario',
                    legend=dict(x=1, y=1),
                    template='plotly_dark'
    )
    return fig


def crear_dem_graphstack_rol_edad(df_in, width=600, height=450):
    # Agrupamos por 'ROL' y 'EDAD_GRUPO'
    df = df_in.copy()
    df_agrupado = df.groupby(['ROL', 'EDAD_GRUPO']).size().unstack()
    # Sumamos las filas y aplicamos un sort
    df_agrupado['suma'] = df_agrupado.sum(axis=1)
    df_agrupado.sort_values('suma', ascending=False, inplace=True)
    df_agrupado.drop(columns='suma', inplace=True)
    # Crea una grafica de barras tipo stacked
    fig = go.Figure(data=[
        go.Bar(name=col, x=df_agrupado.index, y=df_agrupado[col]) for col in df_agrupado.columns
    ])
    # Configuramos el layout
    fig.update_layout(barmode='stack', xaxis_title='Rol de Victima', yaxis_title='Victimas',
                    title='Victimas por Rol y Grupo Etario',
                    autosize=False, width=width, height=height,
                    legend_title='Grupo Etario',
                    legend=dict(x=1, y=1),
                    template='plotly_dark'
    )
    return fig



####  Funciones de 'Lugar de Hechos'  ####


def crear_ub_graphpie_tipocalle(df_in, width=500, height=400):
    # Crea una grafica Pie-chart
    # Primero filtramos fuera los datos nulos
    df = df_in[df_in['TIPO_DE_CALLE'].notna()]
    fig = go.Figure(data=[go.Pie(labels=df['TIPO_DE_CALLE'],
                                values=df['N_VICTIMAS'],
                                rotation=90,
                                textposition='outside'
    )])
    # Configuramos el layout
    fig.update_layout(title='Proporción Victimas por Tipo de Calle',
                    autosize=False, width=500, height=380,
                    legend=dict(x=1, y=1),
                    legend_title='Tipo de Calle',
                    template='plotly_dark'
    )
    return fig


def crear_ub_graphpie_cruce(df_in, width=500, height=400):
    # Crea una grafica Pie-chart
    # Crea la grafica
    fig = go.Figure(data=[go.Pie(labels=df_in['Cruce'],
                                values=df_in['N_VICTIMAS'],
                                rotation=90,
                                textposition='outside'
    )])
    # Configuramos el layout
    fig.update_layout(title='Proporción Victimas en Cruces',
                    autosize=False, width=width, height=height,
                    legend=dict(x=1, y=1),
                    legend_title='En cruce',
                    template='plotly_dark'
    )
    return fig


def crear_ub_graphpareto_comuna(df_in, width=500, height=400):
    def crear_grafica_pareto(df_input: pd.DataFrame, col: str) -> go.Figure:
        """Devuelve un objeto de la clase go.Figure de una grafica de 
        Distribución de Pareto.
        """
        df = df_input.copy()
        data = [go.Bar(
            name = "Victimas",  
            x= df.index,
            y= df[f'{col}_count'], 
            marker= {"color": list(np.repeat('rgb(71, 71, 135)', 5)) + list(np.repeat('rgb(112, 111, 211)', len(df.index) - 5))}
            ),
            go.Scatter(
            line= {"color": "rgb(192, 57, 43)","width": 3}, 
            name= "Porcentage",x=  df.index,y= df['cumulative'],yaxis= "y2",
            mode='lines+markers'
            ),
        ]
        layout = {
        "title": {'text': f"Distribución de Pareto - Comunas"}, 
        "margin": {"b": 20,"l": 50,"r": 50,"t": 10}, 
        "legend": {"x": 0.6,"y": 1.2,'orientation': 'h',
        },
        # axis-Y 1
        "yaxis": {"title": f"Victimas"}, 
        # axis-Y 2
        "yaxis2": {"side": "right","range": [0, 100],"title": f"Porcentaje","overlaying": "y","ticksuffix": " %",}, 
        }
        # Crear grafica
        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(
                    autosize=False, width=width, height=height,
                    template='plotly_dark'
        )
        return fig

    # Primeros Crea un dataframe nuevo con los datos requeridos
    col = 'COMUNA'
    grp = df_in.groupby([col])[col].count()
    df = pd.DataFrame(grp)
    df.index.name = ''
    df = df.sort_values(by=[col], ascending=False)
    count = df_in[col].value_counts().rename(f'{col}_count')
    percentage = df_in[col].value_counts(normalize=True).rename(f'{col}_percentage') * 100
    df = pd.concat([count, percentage], axis=1)
    names_group = list(df.index)
    df['cumulative'] = 0
    iter_n = 0
    for n, name in enumerate(names_group):
        if n == 0:
            df.loc[name, ['cumulative']] = df.loc[names_group[n], [f'{col}_percentage']][0]
        else:
            df.loc[name, ['cumulative']] = df.loc[names_group[iter_n], ['cumulative']][0] + df.loc[names_group[n], [f'{col}_percentage']][0]
            iter_n += 1
    # Crea grafica de Pareto
    fig = crear_grafica_pareto(df, col)
    return fig


def crear_ub_graphstack_franja_calle(df_in, width=500, height=400):
    # Agrupamos por 'Franja_Hora' y 'TIPO_DE_CALLE'
    df_agrupado = df_in.groupby(['Franja_Hora', 'TIPO_DE_CALLE']).size().unstack()
    # Crea una grafica de barras tipo stacked
    fig = go.Figure(data=[
        go.Bar(name=col, x=df_agrupado.index, y=df_agrupado[col]) for col in df_agrupado.columns
    ])
    # Configuramos el layout
    fig.update_layout(barmode='stack', xaxis_title='Franja Hora', yaxis_title='Victimas',
                    title='Victimas por Franja Hora y Tipo de Calle',
                    autosize=False, width=width, height=height,
                    legend=dict(x=1, y=1),
                    legend_title='Tipo de Calle',
                    template='plotly_dark'
    )
    return fig


def crear_ub_graphstack_diasemana_calle(df_in, width=500, height=400):
    # Agrupamos por 'VICTIMA' y 'EDAD_GRUPO'
    df_agrupado = df_in.groupby(['DIA_DE_SEMANA', 'TIPO_DE_CALLE']).size().unstack()
    # Creamos una grafica de barras tipo stacked
    fig = go.Figure(data=[
        go.Bar(name=col, x=df_agrupado.index, y=df_agrupado[col]) for col in df_agrupado.columns
    ])
    # Configuramos el layout
    fig.update_layout(barmode='stack', xaxis_title='Franja Hora', yaxis_title='Victimas',
                    title='Victimas por Día de Semana y Tipo de Calle',
                    autosize=False, width=width, height=height,
                    legend=dict(x=1, y=1),
                    legend_title='Tipo de Calle',
                    template='plotly_dark'
    )
    return fig