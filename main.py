from src.edu_bigdata.static.dataBase import DataBase
import pandas as pd

def main():
    # Ruta a tu archivo CSV principal
    ruta_csv = "src/edu_bigdata/static/csv/GACTT_RESULTS_ANONYMIZED_v2.csv"
    nombre_tabla = "gactt_results_anonymized_v2"

    # Leer el CSV
    df = pd.read_csv(ruta_csv)
    print("✅ Datos leídos del CSV:")
    print(df.shape)
    print(df.head())

    # Insertar en la base de datos
    database = DataBase()
    database.insert_data(df, nombre_tabla)
    print(f"✅ Datos insertados en la tabla '{nombre_tabla}'.")

    # Leer desde la base de datos para verificar
    df_2 = database.read_data(nombre_tabla)
    print("✅ Datos leídos desde la base de datos:")
    print(df_2.shape)
    print(df_2.head())

if __name__ == "__main__":
    main()
