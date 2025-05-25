import pandas as pd
import datetime

class DataWeb:
    """
    Clase para extraer datos desde un archivo local (CSV) en vez de la web.
    """

    def __init__(self, ruta_csv="src/edu_bigdata/static/csv/GACTT_RESULTS_ANONYMIZED_v2.csv"):
        self.ruta_csv = ruta_csv

    def obtener_datos(self):
        """
        Lee datos desde un archivo CSV local.
        """
        try:
            df = pd.read_csv(self.ruta_csv)
            print(f"[INFO] Datos leídos desde {self.ruta_csv}")
            return df
        except Exception as e:
            print(f"[ERROR] No se pudo leer el archivo: {e}")
            return pd.DataFrame()

    def convertir_numericos(self, df=pd.DataFrame()):
        """
        Si necesitas convertir columnas a valores numéricos, adáptalo aquí.
        (Aquí te pongo un ejemplo sencillo, puedes dejarlo vacío si no necesitas nada especial).
        """
        # Ejemplo: convierte las columnas 'col1', 'col2' a numéricas (ajusta según tu archivo)
        # columnas_a_convertir = ['col1', 'col2']
        # for col in columnas_a_convertir:
        #     if col in df.columns:
        #         df[col] = pd.to_numeric(df[col], errors='coerce')
        return df
