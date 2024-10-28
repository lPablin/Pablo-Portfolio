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
    ratings_dict[year] = pd.read_csv("./content/ratings_" + year + ".csv", sep=',')
players=pd.read_csv("./content/players.csv", sep=',')
# Ahora puedes acceder a los DataFrames por el año, por ejemplo:
#ratings_2015 = ratings_dict["2015"]

countries = players['federation'].unique()
country_selected='PER'
year_birth = list(range(1999, 2007))
num_female_players=[]
number_topplayerss=10
for i in year_birth:
  top_players=spanish_ratings2020_year(ratings_dict["2020"],players,2020,i,country=country_selected,number_topplayers=number_topplayerss)
  num_female_players.append(top_players[top_players['gender'] == 'F'].shape[0])
print(num_female_players)
plt.bar(year_birth,num_female_players)
plt.xlabel("Year of birth")
plt.xticks(year_birth[::2])
plt.ylabel("Female national players in top 10 before COVID")
plt.show()
