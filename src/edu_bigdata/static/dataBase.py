import os
import sqlite3
import pandas as pd

class DataBase:
    def __init__(self, db_path="src/edu_bigdata/static/db/cafe_estudio.sqlite"):
        self.db_name = db_path
        os.makedirs(os.path.dirname(self.db_name), exist_ok=True)

    def insert_data(self, df=pd.DataFrame(), nom_table="tabla"):
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

    def update_data(self, nom_table, set_clause, where_clause="1=1"):
        try:
            with sqlite3.connect(self.db_name) as conn:
                query = f"UPDATE {nom_table} SET {set_clause} WHERE {where_clause}"
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
            print(f"Datos actualizados en '{nom_table}' con condición: {where_clause}")
        except Exception as e:
            print(f"Error al actualizar datos:", e)

    def delete_data(self, nom_table, where_clause="1=1"):
        try:
            with sqlite3.connect(self.db_name) as conn:
                query = f"DELETE FROM {nom_table} WHERE {where_clause}"
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
            print(f"Registros eliminados de '{nom_table}' con condición: {where_clause}")
        except Exception as e:
            print(f"Error al eliminar datos:", e)
