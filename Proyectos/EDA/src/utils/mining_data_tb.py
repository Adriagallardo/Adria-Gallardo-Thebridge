#Este archivo tiene las funciones asociadas al data wrangling que elaboramos en el proyecto.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def null_in_dataframe(data): 
    """Esta función retorna el número de valores nulos que tiene el dataframe"""
    a = data.isnull().sum().sum()

    if a > 0:
        print(f"El dataframe tiene {a} valores nulos.")
    
    else:
        print("El dataframe no contiene valores nulos.")

def dulicate_in_dataframe(data):
    """Esta función retorna el número de valores nulos que tiene el dataframe"""
    return data[data.duplicated()]

def outlier_clean(data):
    """Esta función limpia de outliers un dataframe"""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = (Q1 - 1.5 * IQR)
    limite_superior = (Q3 + 1.5 * IQR)
    limite_superior
    data_clean = data[~((data < limite_inferior) | (data > limite_superior)).any(axis=1)]
    print(data_clean.shape)
    return data

def conc_columns(data, name_column, list_column):
    """Esta función genera una nueva columna a partir de las columnas que deseemos de un dataframe"""
    data[name_column] = 0
    for column in list_column:
        data[name_column] += data[column]   

    return data

def check_columns_unique(data):
    """Esta función imprime los valores únicos que nos encontramos para cada columna en un dataframe"""
    for col in data:
        print(f"La columna {col} tiene estos valores únicos:", data[col].unique())

def bin_obj_to_int(data):    
    for col in data:
        """Esta función cambia los valores binarios de tipo objeto a valores binarios de tipo int en un dataframe"""
        if len(data[col].unique()) == 2:
            change = {data[col].unique()[0]: 0, data[col].unique()[1]: 1}
            data[col] = [change[item] for item in data[col]]
        else:
            pass
