import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import random

def num_variable(digitos):
    """This function returns a random number in format string with length as parameter."""
    n = ""
    for i in range(digitos):
        n = n + str(random.randint(1,9))
    return n

def open_file(path_file):
    """
    Read a json file

    Args:
        path_file ([str]): Path where is the file
    """
    with open(path_file, 'r+') as outfile:
        json_data_indented_readed = json.load(outfile)
    return json_data_indented_readed

def mean_visualization():
    """Draw the mean in a plot"""
    #Inacabada
    return None

def df_show_columns(dataframe):
    "This function prints separately all the values in columns"
    for columna in dataframe.columns.values:
        print(dataframe[columna].values)
        print("----------")

def show_list_of_elements(lista):
    """This function prints separately every element in list"""
    for elem in lista:
        print(elem)

def cap_strings():
    """This function capitalize whole strings in pandas"""
    cap = lambda x:x.upper()
    return cap

def multiply(x, multiplicator):
    """This function operates multiplication of first number per number selected"""
    if isinstance(x,int) or isinstance (x, float):
        return x * multiplicator
    return x