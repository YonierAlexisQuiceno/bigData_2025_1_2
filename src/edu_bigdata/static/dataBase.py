import os
import sqlite3
import requests
import datetime
import pandas as pd

class DataBase:
    def __init__(self):
        self.db_name = "src/edu_bigdata/static/db/cafe_estudio.sqlite"

    def insert_data(self, df=pd.DataFrame(), nom_table="tabla"):
        try:
            conn = sqlite3.connect(self.db_name)
            df.to_sql(name=nom_table, con=conn, if_exists='replace', index=False)
            conn.close()
            print(f"✅ Datos insertados en la tabla '{nom_table}'.")
        except Exception as e:
            print("❌ Error al guardar los datos:", e)

    def read_data(self, nom_table=""):
        df = pd.DataFrame()
        try:
            if nom_table:
                conn = sqlite3.connect(self.db_name)
                query = f"SELECT * FROM {nom_table}"
                df = pd.read_sql_query(sql=query, con=conn)
                conn.close()
                return df
        except Exception as e:
            print("❌ Error al obtener los datos:", e)
            return df

    def insert_all_csvs(self, csv_folder="src/edu_bigdata/static/csv"):
        try:
            for file in os.listdir(csv_folder):
                if file.endswith(".csv"):
                    path = os.path.join(csv_folder, file)
                    table = os.path.splitext(file)[0].lower().replace("-", "_")
                    df = pd.read_csv(path)
                    self.insert_data(df=df, nom_table=table)
            print("✅ Todos los CSV se insertaron en la base de datos.")
        except Exception as e:
            print("❌ Error cargando los CSV:", e)
