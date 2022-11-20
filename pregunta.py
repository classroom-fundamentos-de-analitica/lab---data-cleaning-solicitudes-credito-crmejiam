"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", encoding="utf-8", index_col=0)
    #
    # Inserte su código aquí
    #
    df = df.dropna(axis = 0)
    for column in df.columns:
        if (df[column].dtype not in ['int64', 'float64']):
            df[column] = df[column].apply(str.lower)
            df[column] = df[column].apply(lambda x: x.replace("-", " "))
            df[column] = df[column].apply(lambda x: x.replace("_", " "))
            df[column] = df[column].apply(str.strip)
        if (column == "monto_del_credito"):
            df[column] = df[column].apply(lambda x: x.replace(",", ""))
            df[column] = df[column].apply(lambda x: x.replace("$", ""))
            df[column] = df[column].apply(lambda x: x.replace(".00", ""))
            df[column] = df[column].apply(lambda x: int(x))
        if (column == "comuna_ciudadano"):
            df[column] = df[column].apply(lambda x: float(x))
        if (column == "fecha_de_beneficio"):
            df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/",x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    df = df.drop_duplicates().reset_index(drop=True)

    return df