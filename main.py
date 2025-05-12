from src.edu_bigdata.static.dataBase import DataBase
import pandas as pd

def main():
    ruta_csv = "src/edu_bigdata/static/csv/GACTT_RESULTS_ANONYMIZED_v2.csv"
    nombre_tabla = "gactt_results_anonymized_v2"

    df = pd.read_csv(ruta_csv)
    print("[INFO] Datos leídos del CSV:")
    print(df.shape)

    db = DataBase()

    # CREATE
    db.insert_data(df, nombre_tabla)

    # READ
    data = db.read_data(nombre_tabla)
    print("[INFO] Lectura de datos completada")

    # UPDATE: ejemplo - cambia 'Political Affiliation' a 'Ninguna' donde esté vacía
    db.update_data(nombre_tabla, "Political_Affiliation = 'Ninguna'", "Political_Affiliation IS NULL")

    # DELETE: ejemplo - elimina registros sin edad
    db.delete_data(nombre_tabla, "`What is your age?` IS NULL")

    # Confirmación final
    data_final = db.read_data(nombre_tabla)
    print("[INFO] Resultado final después de UPDATE y DELETE:")
    print(data_final.head())

if __name__ == "__main__":
    main()
