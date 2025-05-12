from src.edu_bigdata.static.dataBase import DataBase
import pandas as pd

def main():
    ruta_csv = "src/edu_bigdata/static/csv/GACTT_RESULTS_ANONYMIZED_v2.csv"
    nombre_tabla = "gactt_results_anonymized_v2"

    df = pd.read_csv(ruta_csv)
    print("[INFO] Datos leídos del CSV:")
    print(df.shape)
    print(df.head())

    database = DataBase()
    database.insert_data(df, nombre_tabla)
    print(f"[INFO] Datos insertados en la tabla '{nombre_tabla}'.")

    df_2 = database.read_data(nombre_tabla)
    print("[INFO] Datos leídos desde la base de datos:")
    print(df_2.shape)
    print(df_2.head())

if __name__ == "__main__":
    main()
