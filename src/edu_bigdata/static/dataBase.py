import os
import sqlite3
import pandas as pd

class DataBase:
    """
    Clase para la gestión de datos en una base SQLite.
    Permite insertar DataFrames, leer tablas y cargar múltiples CSV automáticamente.
    """

    def __init__(self, db_path="src/edu_bigdata/static/db/cafe_estudio.sqlite"):
        self.db_name = db_path
        os.makedirs(os.path.dirname(self.db_name), exist_ok=True)

    def insert_data(self, df=pd.DataFrame(), nom_table="tabla"):
        """
        Inserta un DataFrame en la base de datos como una tabla.
        Reemplaza la tabla si ya existe.
        """
        try:
            if df.empty:
                print(f"DataFrame vacío. No se insertó en la tabla '{nom_table}'.")
                return
            with sqlite3.connect(self.db_name) as conn:
                df.to_sql(name=nom_table, con=conn, if_exists='replace', index=False)
            print(f"Datos insertados en la tabla '{nom_table}' ({df.shape[0]} filas).")
        except Exception as e:
            print(f"Error al guardar los datos en '{nom_table}':", e)

    def read_data(self, nom_table=""):
        """
        Lee una tabla de la base de datos y la retorna como DataFrame.
        """
        try:
            if not nom_table:
                raise ValueError("Debes proporcionar un nombre de tabla.")
            with sqlite3.connect(self.db_name) as conn:
                query = f"SELECT * FROM {nom_table}"
                df = pd.read_sql_query(query, conn)
            print(f"Consulta completada: {nom_table} ({df.shape[0]} filas).")
            return df
        except Exception as e:
            print(f"Error al leer los datos de '{nom_table}':", e)
            return pd.DataFrame()

    def insert_all_csvs(self, csv_folder="src/edu_bigdata/static/csv"):
        """
        Inserta todos los archivos CSV de una carpeta en la base de datos.
        Usa el nombre del archivo (sin extensión) como nombre de tabla.
        """
        try:
            archivos = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]
            if not archivos:
                print("No se encontraron archivos CSV en la carpeta.")
                return

            for file in archivos:
                path = os.path.join(csv_folder, file)
                table = os.path.splitext(file)[0].lower().replace("-", "_")
                df = pd.read_csv(path)
                self.insert_data(df=df, nom_table=table)

            print("Todos los archivos CSV fueron insertados en la base de datos.")
        except Exception as e:
            print("Error al insertar CSVs en la base de datos:", e)
