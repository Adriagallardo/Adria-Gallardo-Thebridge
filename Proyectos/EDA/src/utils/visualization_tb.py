#Este archivo contiene las funciones de visualización (pandas, matplolib y seaborn) que elaboramos en el proyecto.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def read_my_csv(file_path):
    """Esta función lee el un archivo .csv introduciendo su ruta"""
    data = pd.read_csv(file_path)
    return data

def sns_gstyle():
    """Esta función cambia los gráficos de seaborn que vienen por defecto"""
    sns.set(style="ticks")

#def alcohol_columns_intro():
#    ""Esta función introduce al usuario al significado de las columnas así
#    como al valor que nos otorgan, de los datasets encontrados"""
#    print("-Escuela: escuela del estudiante(binario: 'GP'- Gabriel Pereira o 'MS'- Mousinho da Silveira)")
#    print("-Sexo: sexo del estudiante (binario: 'F'- femenino o 'M'- masculino)")
#    print("-Edad: edad del estudiante (numérico: del 15 al 22)")
#    print("-Dirección: tipo de zona de residencia (binario: 'U'- urbano o 'R'- rural)")
#    print("-Tamaño_familia: tamaño de la familia (binario: 'LE3'- menor o igual a 3 o 'GT3'- mayor que 3)")
#    print("-Par_Estado: estado de relación de padres (binario: 'T'- viven juntos o 'A'- viven separados) ")
#    print("-M_edu: nivel educativo de la madre (numérico: del 0 siendo este el menor (sin estudios) al 4 (con estudios superiores a secundaria)")
#    print("-P_edu: nivel educativo del padre (numérico: del 0 siendo este el menor (sin estudios) al 4 (con estudios superiores a secundaria)")
#    print("-M_trab: trabajo de la madre (nominal: 'educación', 'salud', servicio 'civil', 'en_casa' o otro)")
#    print("-P_trab: trabajo del padre (nominal: 'educación', 'salud', servicio 'civil', 'en_casa' o otro)")
#    print("-Razon: razon para escoger escuela (nominal: cerca de 'casa', 'reputación' de escuela, preferencias de 'curso', otros )")
#    print("-Guardian")

def alcohol_columns_intro():
    """Esta función introduce al usuario al significado de las columnas así
    como al valor que nos otorgan, de los datasets encontrados"""

    print("-school: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)")
    print("-sex: Student's sex (binary: 'F' - female or 'M' - male)")
    print("-age: Student's age (numeric: from 15 to 22)")
    print("-address: Student's home address type (binary: 'U' - urban or 'R' - rural)")
    print("-famsize: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)")
    print("-Pstatus: Parent's cohabitation status (binary: 'T' - living together or 'A' - living apart)")
    print("-Medu: Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    print("-Fedu: Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    print("-Mjob: Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    print("-Fjob: Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    print("-reason: Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')")
    print("-guardian: Student's guardian (nominal: 'mother', 'father' or 'other')")
    print("-traveltime: Home to school travel time (numeric: 1 - &lt;15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - &gt;1 hour)")
    print("-studytime: Weekly study time (numeric: 1 - &lt;2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - &gt;10 hours)")
    print("-failures: Number of past class failures (numeric: n if 1&lt;=n&lt;3, else 4)")
    print("-schoolsup: Extra educational support (binary: yes or no)")
    print("-famsup: Family educational support (binary: yes or no)")
    print("-paid: Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)")
    print("-activities: Extra-curricular activities (binary: yes or no)")
    print("-nursery: Attended nursery school (binary: yes or no)")
    print("-higher: Wants to take higher education (binary: yes or no)")
    print("-internet: Internet access at home (binary: yes or no)")
    print("-romantic: With a romantic relationship (binary: yes or no)")
    print("-famrel: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent")
    print("-freetime: Free time after school (numeric: from 1 - very low to 5 - very high)")
    print("-goout: Going out with friends (numeric: from 1 - very low to 5 - very high)")
    print("-Dalc: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    print("-Walc: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    print("-health: Current health status (numeric: from 1 - very bad to 5 - very good)")
    print("-absences: Number of school absences (numeric: from 0 to 93)")
    print("-G1: First period grade (numeric: from 0 to 20)")
    print("-G2: Second period grade (numeric: from 0 to 20)")
    print("-G3: Final grade (numeric: from 0 to 20, output target)")

def alcohol_column_intro(column):
    
    if column == "school":
        print("-school: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)")
    elif column == "sex":
        print("-sex: Student's sex (binary: 'F' - female or 'M' - male)")
    elif column == "age":
        print("-age: Student's age (numeric: from 15 to 22)")
    elif column == "address":
        print("-address: Student's home address type (binary: 'U' - urban or 'R' - rural)")
    elif column == "famsize":
        print("-famsize: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)")
    elif column == "Pstatus":
        print("-Pstatus: Parent's cohabitation status (binary: 'T' - living together or 'A' - living apart)")
    elif column == "Medu":
        print("-Medu: Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    elif column == "Fedu":
        print("-Fedu: Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    elif column == "Mjob":
        print("-Mjob: Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    elif column == "Fjob":
        print("-Fjob: Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    elif column == "reason":
        print("-reason: Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')")
    elif column == "guardian":
        print("-guardian: Student's guardian (nominal: 'mother', 'father' or 'other')")
    elif column == "traveltime":
        print("-traveltime: Home to school travel time (numeric: 1 - &lt;15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - &gt;1 hour)")
    elif column == "studytime":
        print("-studytime: Weekly study time (numeric: 1 - &lt;2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - &gt;10 hours)")
    elif column == "failures":
        print("-failures: Number of past class failures (numeric: n if 1&lt;=n&lt;3, else 4)")
    elif column == "schoolsup":
        print("-schoolsup: Extra educational support (binary: yes or no)")
    elif column == "famsup":
        print("-famsup: Family educational support (binary: yes or no)")
    elif column == "paid":
        print("-paid: Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)")
    elif column == "activities":
        print("-activities: Extra-curricular activities (binary: yes or no)")
    elif column == "nursery":
        print("-nursery: Attended nursery school (binary: yes or no)")
    elif column == "higher":
        print("-higher: Wants to take higher education (binary: yes or no)")
    elif column == "internet":
        print("-internet: Internet access at home (binary: yes or no)")
    elif column == "romantic":
        print("-romantic: With a romantic relationship (binary: yes or no)")
    elif column == "famrel":
        print("-famrel: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent")
    elif column == "freetime":
        print("-freetime: Free time after school (numeric: from 1 - very low to 5 - very high)")
    elif column == "goout":
        print("-goout: Going out with friends (numeric: from 1 - very low to 5 - very high)")
    elif column == "Dalc":
        print("-Dalc: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    elif column == "Walc":
        print("-Walc: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    elif column == "health":
        print("-health: Current health status (numeric: from 1 - very bad to 5 - very good)")
    elif column == "absences":
        print("-absences: Number of school absences (numeric: from 0 to 93)")
    elif column == "G1":
        print("-G1: First period grade (numeric: from 0 to 20)")
    elif column == "G2":
        print("-G2: Second period grade (numeric: from 0 to 20)")
    elif column == "G3":
        print("-G3: Final grade (numeric: from 0 to 20, output target)")
    
def corr_onevalue_graphic(data, variable):
    """Esta función un muestra un gráfico para un Series correspondiente a un mostreo de correlación
    de una columna con las demás del dataframe. No estudia la negatividad o positividad de los valores
    ya que trabaja con valores absolutos"""
    plt.figure(figsize=(12,9))
    current_palette = sns.color_palette("tab10")
    data.abs().sort_values()[:-1].plot.bar(width=1,color=current_palette, rot=60)
    plt.title(f"Correlación de las variables en estudio con {variable}")
    plt.ylabel('Coeficiente de correlación en valor absoluto')
    plt.xlabel('Variables en estudio')