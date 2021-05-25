#Este archivo contiene las funciones del proyecto utilizadas para abrir, crear, leer y escribir archivos que se llevan a cabo en el proyecto.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def read_my_csv(file_path):
    """Esta función lee el un archivo .csv introduciendo su ruta"""
    data = pd.read_csv(file_path)
    return data