import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Cambia el backend de Matplotlib para evitar el uso de Tkinter
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def spanish_ratings2020_year(nombre_ratings_year,players,year,birth_year,country='ESP',number_topplayers=25):
  month=1
  January_year = nombre_ratings_year[(nombre_ratings_year['year'] == year) & (nombre_ratings_year['month'] == month)]
  #spanish_players = players[(players['federation'] == 'ESP')&(players['yob'].between(2003,2004))]
  spanish_players = players[(players['federation'] == country)&(players['yob']== birth_year)]
  merged_spanish_players_2020 = pd.merge(January_year, spanish_players, on='fide_id')
  top_players = merged_spanish_players_2020.nlargest(number_topplayers, 'rating_standard')[['name', 'gender','yob', 'rating_standard']]
  top_players['position'] = range(1, number_topplayers+1)
  top_players = top_players.reset_index(drop=True)
  return top_players
"""
January_2020 = ratings_2020[(ratings_2020['year'] == year) & (ratings_2020['month'] == month)]
merged_data = pd.merge(January_2020, players, on='fide_id')
filtered_data = merged_data[(merged_data['yob'] == 2006) & (merged_data['rating_standard']>1300)]
"""
def total_players(nombre_ratings_year,players,year,birth_year,country='ESP'):
  
  month=1
  January_year = nombre_ratings_year[(nombre_ratings_year['year'] == year) & (nombre_ratings_year['month'] == month)& (nombre_ratings_year['rating_standard']>1300)]
  #spanish_players = players[(players['federation'] == 'ESP')&(players['yob'].between(2003,2004))]

  spanish_players = players[(players['federation'] == country)&(players['yob']== birth_year)]
  merged_spanish_players_2020 = pd.merge(January_year, spanish_players, on='fide_id')
  return merged_spanish_players_2020

# Función que genera el gráfico
def generate_plot(ratings,players,country_selected, year_range, number_topplayerss=10):
    year_birth = list(year_range)
    num_female_players = []
    
    try:
        for i in year_birth:
            # Aquí es donde puede ocurrir el error si no hay datos suficientes
            top_players = spanish_ratings2020_year(ratings, players, 2020, i, country=country_selected, number_topplayers=number_topplayerss)
            num_female_players.append(top_players[top_players['gender'] == 'F'].shape[0])
        
        # Si todo va bien, generamos el gráfico
        plt.figure(figsize=(10, 6))
        plt.bar(year_birth, num_female_players)
        plt.xlabel("Year of birth")
        plt.xticks(year_birth[::2])
        plt.ylabel(f"Female national players from {country_selected}")
        plt.title(f"Top 10 Female Players in {country_selected}")

        # Guardar el gráfico en un objeto de memoria en base64
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        
        return 'data:image/png;base64,{}'.format(graph_url)

    except Exception as e:
        # Aquí puedes devolver un mensaje amigable o una imagen indicando que no hay datos
        print(f"Error generando el gráfico: {e}")  # Esto lo puedes usar para depuración

        # Devolver un mensaje de error o una imagen de "no datos"
        return None

def generate_table(ratings, players, year_range, number_topplayerss):
    # Filtramos los jugadores del país y el rango de años
    # Aquí replicamos parte de la lógica que ya usas en `mapamundi_ELO`
    # para generar la tabla en función del país y el rango de años seleccionado.

    # Filtrar datos para enero de 2020
    year = 2020
    month = 1
    January_2020 = ratings[(ratings['year'] == year) & (ratings['month'] == month)]
    
    # Hacemos merge de los ratings con los jugadores
    merged_data = pd.merge(January_2020, players, on='fide_id')
    
    # Filtrar jugadores del año de nacimiento entre el rango seleccionado
    filtered_data = merged_data[(merged_data['yob'] == year_range[-1]-1) & (merged_data['rating_standard']>1300)]
    
    # Contar el número de jugadores por país
    players_by_country = filtered_data.groupby('federation').size().reset_index(name='num_players')
    
    # Contar el número de jugadores por país
    players_by_country = filtered_data.groupby('federation').size().reset_index(name='num_players')

    # Seleccionar los países con más de 50 jugadores nacidos en 2010 con ELO
    countries_with_plus_players = players_by_country[players_by_country['num_players'] >= 20]
    
    # Calcular métricas (por ejemplo, promedio de jugadoras femeninas en el top 10 y el ratio mujeres)
    countries = countries_with_plus_players['federation'].tolist()
    number_female = []
    numberofplayers = []
    desviacion_tipica_final = []
    ratio_women = []

    for country in countries:
        female_average = []
        ratiowomen = []
        numberofplayersyear = []

        for years in year_range:
            # Obtén los top jugadores del país y año especificado
            top_players = spanish_ratings2020_year(ratings, players, year,years, country=country, number_topplayers=number_topplayerss)
            
            # Calcular el promedio de mujeres en el top 10
            female_average.append(top_players[top_players['gender'] == 'F'].shape[0] / 10)
            
            # Calcular el ratio de mujeres entre los jugadores totales
            totalplayers = total_players(ratings, players, year,years, country=country)
            ratiowomen.append(totalplayers[totalplayers['gender'] == 'F'].shape[0] / totalplayers.shape[0])
            
            numberofplayersyear.append(totalplayers.shape[0])

        # Calcular la media y desviaciones
        mu_A = sum(female_average) / len(female_average)
        mu_B = sum(ratiowomen) / len(ratiowomen)

        number_female.append(mu_A)
        ratio_women.append(mu_B)

        variance_ratio = (mu_A / mu_B) ** 2 * (((np.var(female_average)) ** 0.5 / mu_A) ** 2 + ((np.var(ratiowomen)) ** 0.5 / mu_B) ** 2)
        desviacion_tipica_final.append(np.sqrt(variance_ratio))
        numberofplayers.append(int(sum(numberofplayersyear) / len(numberofplayersyear)))

    # Agregar las métricas a la tabla
    countries_with_plus_players['average_per_year_num_players'] = numberofplayers
    countries_with_plus_players['average_women_in_top'] = np.array(number_female) * 10
    countries_with_plus_players['desviation'] = desviacion_tipica_final
    countries_with_plus_players['ratio_women'] = ratio_women
    countries_with_plus_players['top_players/ratio_women'] = countries_with_plus_players['average_women_in_top'] / countries_with_plus_players['ratio_women'] / number_topplayerss

    # Ordenar los datos por la columna 'top10/ratio_women'
    data_sorted_by_female = countries_with_plus_players.sort_values(by=['top_players/ratio_women'], ascending=False)

    data_sorted_by_female.index = range(1, len(data_sorted_by_female) + 1)
    # Convertir la tabla a HTML
    table_html = data_sorted_by_female.to_html(classes="table table-striped", index=True)

    return table_html

def generate_mapamundi(ratings, players, year_range, number_topplayerss):
    # Filtramos los jugadores del país y el rango de años
    # Aquí replicamos parte de la lógica que ya usas en `mapamundi_ELO`
    # para generar la tabla en función del país y el rango de años seleccionado.

    # Filtrar datos para enero de 2020
    year = 2020
    month = 1
    January_2020 = ratings[(ratings['year'] == year) & (ratings['month'] == month)]
    
    # Hacemos merge de los ratings con los jugadores
    merged_data = pd.merge(January_2020, players, on='fide_id')
    
    # Filtrar jugadores del año de nacimiento entre el rango seleccionado
    filtered_data = merged_data[(merged_data['yob'] == year_range[-1]-1) & (merged_data['rating_standard']>1300)]
    
    # Contar el número de jugadores por país
    players_by_country = filtered_data.groupby('federation').size().reset_index(name='num_players')
    
    # Contar el número de jugadores por país
    players_by_country = filtered_data.groupby('federation').size().reset_index(name='num_players')

    # Seleccionar los países con más de 50 jugadores nacidos en 2010 con ELO
    countries_with_plus_players = players_by_country[players_by_country['num_players'] >= 20]
    
    # Calcular métricas (por ejemplo, promedio de jugadoras femeninas en el top 10 y el ratio mujeres)
    countries = countries_with_plus_players['federation'].tolist()
    number_female = []
    numberofplayers = []
    ratio_women = []

    for country in countries:
        female_average = []
        ratiowomen = []
        numberofplayersyear = []

        for years in year_range:
            # Obtén los top jugadores del país y año especificado
            top_players = spanish_ratings2020_year(ratings, players, year,years, country=country, number_topplayers=number_topplayerss)
            
            # Calcular el promedio de mujeres en el top 10
            female_average.append(top_players[top_players['gender'] == 'F'].shape[0] / 10)
            
            # Calcular el ratio de mujeres entre los jugadores totales
            totalplayers = total_players(ratings, players, year,years, country=country)
            ratiowomen.append(totalplayers[totalplayers['gender'] == 'F'].shape[0] / totalplayers.shape[0])
            
            numberofplayersyear.append(totalplayers.shape[0])

        # Calcular la media y desviaciones
        mu_A = sum(female_average) / len(female_average)
        mu_B = sum(ratiowomen) / len(ratiowomen)

        number_female.append(mu_A)
        ratio_women.append(mu_B)

        numberofplayers.append(int(sum(numberofplayersyear) / len(numberofplayersyear)))

    # Agregar las métricas a la tabla
    countries_with_plus_players.loc[:,'average_per_year_num_players'] = numberofplayers
    countries_with_plus_players.loc[:,'average_women_in_top'] = np.array(number_female) * 10
    countries_with_plus_players.loc[:,'ratio_women'] = ratio_women
    countries_with_plus_players.loc[:,'top_players/ratio_women'] = countries_with_plus_players['average_women_in_top'] / countries_with_plus_players['ratio_women'] / number_topplayerss

    # Ordenar los datos por la columna 'top10/ratio_women'
    data_sorted_by_female = countries_with_plus_players.sort_values(by=['top_players/ratio_women'], ascending=False)

    data_sorted_by_female.index = range(1, len(data_sorted_by_female) + 1)
    result=data_sorted_by_female[["federation", 'top_players/ratio_women']].head(100).reset_index(drop=True)
    print(result['federation'])
    result.index=result.index+1
    world = gpd.read_file("./geopandas/ne_110m_admin_0_countries.shp")

    # Mostrar las columnas que contienen 'iso' Index(['ISO_A2', 'ISO_A2_EH', 'ISO_A3', 'ISO_A3_EH', 'ISO_N3', 'ISO_N3_EH',
    iso_a3_countries = world['ISO_A3']

    result.replace({'BUL': 'BGR','MAS':'MYS','VIE':'VNM','CHI':'CHL','ENG':'GBR','DEN':'DNK','NLD':'NED','GER':'DEU'}, regex=False,inplace=True)

    #world.loc[world['name'] == 'United Kingdom', 'ISO_A3'] = 'ENG'
    #world.loc[world['name'] == 'Germany', 'ISO_A3'] = 'GER'
    #world.loc[world['name'] == 'Netherlands', 'ISO_A3'] = 'NED'
    world = world.merge(result, left_on='ISO_A3',right_on='federation', how='left')
    print(world['federation'].dropna())
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    plt.rcParams.update({
    'font.size': 14,             # Tamaño de la fuente general
    'axes.titlesize': 16,        # Tamaño de la fuente del título de los ejes
    'axes.labelsize': 14,        # Tamaño de la fuente de las etiquetas de los ejes
    'xtick.labelsize': 12,       # Tamaño de la fuente de las etiquetas de las marcas en el eje x
    'ytick.labelsize': 12,       # Tamaño de la fuente de las etiquetas de las marcas en el eje y
    'legend.fontsize': 14,       # Tamaño de la fuente de la leyenda
    'figure.titlesize': 18       # Tamaño de la fuente del título de la figura
    })
    world.boundary.plot(ax=ax)
    bins=20
    world.plot(column='top_players/ratio_women', ax=ax, legend=True,
           legend_kwds={'label': "Valores por país",
                        'orientation': "horizontal"},
           cmap='plasma',k=bins)
    # Convertir la figura en imagen
    img = io.BytesIO()
    FigureCanvas(fig).print_png(img)
    img.seek(0)

    return img