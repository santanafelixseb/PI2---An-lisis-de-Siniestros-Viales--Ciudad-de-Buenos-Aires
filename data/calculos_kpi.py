"""Calculos de los KPI's, para uso en el dashboard desarrollado con Streamlit.

Los KPI's son:

KPI 1. Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, 
en comparación con la tasa de homicidios en siniestros viales del semestre anterior.
Definimos a la tasa de homicidios en siniestros viales como el número de víctimas fatales
en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período 
de tiempo específico. Su fórmula es: (Número de homicidios en siniestros viales / Población total) * 100,000

KPI 2. Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior.
Definimos a la cantidad de accidentes mortales de motociclistas en siniestros viales como el número absoluto 
de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado 
periodo temporal. Su fórmula para medir la evolución de los accidentes mortales con víctimas en moto es: 
(# de mortales en moto en el año anterior - # de mortales en moto en el año actual) / (# de mortales moto en el año anterior) * 100

KPI 3. Reducir en un 7% la cantidad de accidentes mortales de peatones en el último año, en CABA, respecto al año anterior.
Definimos a la cantidad de accidentes mortales de peatones en siniestros viales como el número absoluto 
de accidentes fatales en los que estuvieron involucradas peatones víctimas  en un determinado periodo temporal. 
Su fórmula para medir la evolución de los accidentes mortales con peatones víctimas: 
(# de mortales peatones en el año anterior - # de mortales peatones en el año actual) / (# de mortales peatones en el año anterior) * 100

Nota sobre fuente de datos:
    La data de poblacion, de la Ciudad Autónoma de Buenos Aires (CABA), proviene de:
    - https://www.argentina.gob.ar/caba

"""

import pandas as pd


# Cargar data de 'df_homicidios.pkl'
df_homicidios: pd.DataFrame = pd.read_pickle('data/df_homicidios.pkl')

poblacion_caba =  3_121_707  # cantidad habitantes en CABA (fuente: https://www.argentina.gob.ar/caba)


# Calculos KPI 1:
# Instanciar un nuevo dataframe para el KPI 1
df_kpi1_tasa = pd.DataFrame()
# Crear nueva columna con total de victimas por semestre
df_kpi1_tasa['total_victimas'] = df_homicidios.groupby(['AAAA', 'SEMESTRE'])['N_VICTIMAS'].sum()
df_kpi1_tasa.reset_index(inplace=True)
# Calcular la tasa de victimas por cada 100,000 habitantes
df_kpi1_tasa['tasa_victimas'] = round((df_kpi1_tasa['total_victimas'] / poblacion_caba) * 100_000, 2)
# Calcular el cambio en tasa
df_kpi1_tasa['cambio_nominal_KPI'] = df_kpi1_tasa['tasa_victimas'].diff().round(2)
# Calcular el cambio porcentual en tasa
df_kpi1_tasa['cambio_porcentual_KPI'] = df_kpi1_tasa['tasa_victimas'].pct_change().multiply(100).round(1)

# Ajustes para datos requerido en los grafos
# Descartar primera fila de df, por no tener data de KPI
df_kpi1_tasa.drop(df_kpi1_tasa.index[0], inplace=True)
# Agregar columna con valor de la meta del KPI
df_kpi1_tasa['meta_KPI'] = -10  # por definicion del KPI
# Agregar columna que indica periodo
df_kpi1_tasa['Periodo'] = df_kpi1_tasa['AAAA'].astype(str) + ' - ' + df_kpi1_tasa['SEMESTRE'].astype(str) + 'º'
# Fijar esta columna con el index
df_kpi1_tasa.set_index('Periodo', inplace=True)


# Calculos KPI 2:
# Filtrar data de df_homicidios donde columna 'VICTIMA' = 'MOTO'
df_homicidios_moto = df_homicidios[df_homicidios['VICTIMA'] =='MOTO']
# Instanciar un nuevo dataframe para el KPI 2
df_kpi2_moto = pd.DataFrame()
# Crear nueva columna con total de victimas por año
df_kpi2_moto['total_victimas'] = df_homicidios_moto.groupby(['AAAA'])['N_VICTIMAS'].sum()
df_kpi2_moto.reset_index(inplace=True)
# Calcular el cambio en cantidad victimas
df_kpi2_moto['cambio_nominal_KPI'] = df_kpi2_moto['total_victimas'].diff().astype('Int64')
# Calcular el cambio porcentual en tasa
df_kpi2_moto['cambio_porcentual_KPI'] = df_kpi2_moto['total_victimas'].pct_change().multiply(100).round(1)

# Ajustes para datos requerido en los grafos
# Descartar primera fila de df, por no tener data de KPI
df_kpi2_moto.drop(df_kpi2_moto.index[0], inplace=True)
# Cambiar a tipo int la columna de 'cambio_nominal_KPI'
df_kpi2_moto['cambio_nominal_KPI'] = df_kpi2_moto['cambio_nominal_KPI'].astype(int)
# Agregar columna con valor de la meta del KPI
df_kpi2_moto['meta_KPI'] = -7  # por definicion del KPI
# Renombrar 'AAAA' a 'Año'
df_kpi2_moto.rename(columns={'AAAA':'Año'}, inplace=True)
# Fijar esta columna con el index
df_kpi2_moto.set_index('Año', inplace=True)


# Calculos KPI 3:
# Filtrar data de df_homicidios donde columna 'VICTIMA' = 'PEATON'
df_homicidios_peaton = df_homicidios[df_homicidios['VICTIMA'] =='PEATON']
# Instanciar un nuevo dataframe para el KPI 3
df_kpi3_peaton = pd.DataFrame()
# Crear nueva columna con total de victimas por año
df_kpi3_peaton['total_victimas'] = df_homicidios_peaton.groupby(['AAAA'])['N_VICTIMAS'].sum()
df_kpi3_peaton.reset_index(inplace=True)
# Calcular el cambio en cantidad victimas
df_kpi3_peaton['cambio_nominal_KPI'] = df_kpi3_peaton['total_victimas'].diff()
# Calcular el cambio porcentual en tasa
df_kpi3_peaton['cambio_porcentual_KPI'] = df_kpi3_peaton['total_victimas'].pct_change().multiply(100).round(1)

# Ajustes para datos requerido en los grafos
# Descartar primera fila de df, por no tener data de KPI
df_kpi3_peaton.drop(df_kpi3_peaton.index[0], inplace=True)
# Cambiar a tipo int la columna de 'cambio_nominal_KPI'
df_kpi3_peaton['cambio_nominal_KPI'] = df_kpi3_peaton['cambio_nominal_KPI'].astype(int)
# Agregar columna con valor de la meta del KPI
df_kpi3_peaton['meta_KPI'] = -7  # por definicion del KPI
# Renombrar 'AAAA' a 'Año'
df_kpi3_peaton.rename(columns={'AAAA':'Año'}, inplace=True)
# Fijar esta columna con el index
df_kpi3_peaton.set_index('Año', inplace=True)


# Almacen de data KPI en disco, para uso en el dashboard desarrollado con Streamlit
df_kpi1_tasa.to_pickle('data/df_kpi1_tasa.pkl')
df_kpi2_moto.to_pickle('data/df_kpi2_moto.pkl')
df_kpi3_peaton.to_pickle('data/df_kpi3_peaton.pkl')