#Este archivo tiene las funciones asociadas al data wrangling que elaboramos en el proyecto.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def null_in_dataframe(data): 
    """Esta función retorna el número de valores nulos que tiene el dataframe"""
    return data.isnull().sum().sum()

def dulicate_in_dataframe(data):
    """Esta función retorna el número de valores nulos que tiene el dataframe"""
    return data[data.duplicated()]

def outlier_clean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = (Q1 - 1.5 * IQR)
    limite_superior = (Q3 + 1.5 * IQR)
    limite_superior
    data_clean = data[~((data < limite_inferior) | (data > limite_superior)).any(axis=1)]
    print(data_clean.shape)
    return data_clean