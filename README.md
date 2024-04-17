# Análisis de Sinietros Viales en la Ciudad de Buenos Aires

## Introducción
Este repositorio contiene un proyecto completo de análisis de datos centrado en las siniestros viales en la ciudad de Buenos Aires. El objetivo de este proyecto es explorar y comprender los factores que contribuyen a los accidentes fatales, visualizar patrones relevantes y desarrollar un panel interactivo utilizando Python y Streamlit.

## Conjunto de Datos
El conjunto de datos utilizado para este análisis incluye información sobre siniestros que resultaron en muertes dentro de Buenos Aires. Contiene detalles como la fecha y hora del accidente, ubicación, tipo de vehículo involucrado, datos demográfico y más.

## Estructura de Carpetas del Proyecto
A continuación se muestra una estructura de carpetas para este proyecto:
```
├── .streamlit/
│   └── config.toml
├── data/
│   ├── calculos_kpi.py
│   └── crear_db.py
├── pages/
│   ├── 01_📈_KPIs.py
│   ├── 02_🕖_Datos_Temporales.py
│   ├── 03_📊_Demográfico.py
│   └── 04_🗺️_Lugar de Hecho.py
├── .gitignore
├── EDA.ipynb
├── Portal.py
├── README.md
├── requirements.txt
├── utils_dashb_graphs.py
└── utils_dashboard.py
```

## Bibliotecas de Python Utilizadas
- Pandas: Para la manipulación y limpieza de datos.
- Matplotlib y Plotly: Para la visualización de gráficos.
- Streamlit: Para crear el panel interactivo.

## Cómo Ejecutar el Panel
1. Clona este repositorio.
2. Instala las dependencias del proyecto utilizando `pip install -r requirements.txt`.
3. Ejecuta el panel con `streamlit run Portal.py`.

## Conclusiones
En el análisis explorativo, observamos los siguientes hechos:
- La mayoría de las víctimas tienen aproximadamente de 20 a 45 años de edad.
- Hay una cantidad de víctimas desproporcionadamente alta de 42 años de edad.
- Hay una proporción mayor de víctimas con rol de conductor.
- Dentro de las víctimas con rol de conductor, la mayoría son jóvenes del grupo etario de 21 a 40 años.
- Los autos, vehículos de carga y vehículos de pasajeros son los acusados más frecuentes.
- La mayoría de las víctimas con edades atípicas son peatones, con edades ≥ 83 años.
