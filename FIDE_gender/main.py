import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import seaborn as sns
from functions import *
# Diccionario para almacenar los DataFrames con el año como clave
ratings_dict = {}

# Cargar los archivos en el diccionario
for i in range(15, 22):
    year = "20" + str(i)
    ratings_dict[year] = pd.read_csv("/content/ratings_" + year + ".csv", sep=',')

# Ahora puedes acceder a los DataFrames por el año, por ejemplo:
ratings_2015 = ratings_dict["2015"]
ratings_2016 = ratings_dict["2016"]
  
players=pd.read_csv("/content/drive/MyDrive/FIDE/players.csv", sep=',')


