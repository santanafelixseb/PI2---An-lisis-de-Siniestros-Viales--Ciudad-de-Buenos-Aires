import os
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import pandas as pd


def crear_database():
    """Crea base de datos de SQLite3 y crea tablas con los datos en
    DataFrames procesados en EDA.ipynb
    """
    # Instanciamos la clase Base de la cual heredan TablaHechos y TablaVictimas
    Base = declarative_base()

    class TablaHechos(Base):
        """Clase que representa la tabla principal 'hechos'
        con una relación uno a muchos con tabla 'victimas'.
        """
        __tablename__ = 'hechos'
        ID = Column(String, primary_key=True)
        N_VICTIMAS = Column(Integer)
        MM = Column(Integer)
        DD = Column(Integer)
        HH = Column(Integer)
        SEMESTRE = Column(Integer)
        DIA_DE_SEMANA = Column(String)
        MES = Column(String)
        FECHA_HORA = Column(DateTime)
        TIPO_DE_CALLE = Column(String)
        Calle = Column(String)
        Direccion = Column(String)
        COMUNA = Column(Integer)
        pos_x = Column('pos x', Float, key='pos_x')
        pos_y = Column('pos y', Float, key='pos_y')
        VICTIMA = Column(String)
        ACUSADO = Column(String)

        # Relación con la tabla secundaria 'victimas'
        children = relationship("TablaVictimas")

    class TablaVictimas(Base):
        """Calse que representa la tabla secundaria 'victimas'
        con una relación muchos a uno con tabla 'hechos'.
        """
        __tablename__ = 'victimas'
        ID_hecho = Column(String, ForeignKey('hechos.ID'), primary_key=True)
        ROL = Column(String)
        VICTIMA = Column(String)
        SEXO = Column(String)
        EDAD = Column(Integer)


    dir_target = 'data/db'  # Nombre de la carpeta a almacenar la base de datos
    # Creamos el directorio si no existe
    os.makedirs(dir_target, exist_ok=True)

    # Creamos un motor que almacena los datos en el archivo 'siniestros_viales_caba.db',
    # en el 'directorio_target'
    engine = create_engine(f'sqlite:///{dir_target}/siniestros_viales_caba.db')

    # Creamos todas las tablas en el motor
    Base.metadata.create_all(engine)

    # Creamos una sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Cargamos los dataframe que contienen la data a cargar a SQLite
    df_hechos = pd.read_pickle('hom_hechos.pkl')
    df_victimas = pd.read_pickle('hom_victimas.pkl')

    # Cargamos la data a la base de datos que creamos
    df_hechos.to_sql('hechos', engine, if_exists='replace')
    df_victimas.to_sql('victimas', engine, if_exists='replace')

    # Le damos commit a la sesión
    session.commit()
    # Cerramos la sesión
    session.close()


if __name__ == '__main__':
    # Crear base de datos
    crear_database()