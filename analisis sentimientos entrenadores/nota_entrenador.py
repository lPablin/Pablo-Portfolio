import pandas as pd

def calcular_puntuacion(row, media_tweets):
    puntuacion = 0

    # Sentimiento Global
    if row['Sentimiento Global'] < 0:
        puntuacion -= 1
    else:
        puntuacion += 1

    # Número de Tweets y Sentimiento Global
    if row['Numero de Tweets'] > media_tweets:
        if row['Sentimiento Global'] < 0:
            puntuacion -= 1
        else:
            puntuacion += 1

    # Resultado
    if row['Resultado'] > 0:
        puntuacion += 1
    elif row['Resultado'] < 0:
        puntuacion -= 1

    # Posición (Descenso y Playoff)
    if row['En Descenso'] == 1:
        puntuacion -= 2
    if row['En Playoff'] == 1:
        puntuacion += 2

    # Distancia al Descenso
    puntuacion += row['Distancia Descenso'] // 3  # Ejemplo: sumar 1 punto por cada 3 puntos de distancia

    # Diferencia de Posiciones
    if row['Diferencia Posiciones'] < -5:
        puntuacion -= 1
    elif row['Diferencia Posiciones'] > 5:
        puntuacion += 1

    # Racha (a partir de la cuarta jornada)
    if row['Jornada'] >= 4:
        if row['Racha'] > 6:
            puntuacion += 1
        elif row['Racha'] < 3:
            puntuacion -= 1

    return puntuacion

año=2024
equipo_seleccionado= 'Huesca'
entrenador='ziganda'
anio = "2023"
df_combined = pd.read_csv(entrenador+'_'+equipo_seleccionado+'_analisis_partidos.csv')

# Calcular la media de tweets para comparación
media_tweets = df_combined['Numero de Tweets'].mean()

# Aplicar la función al DataFrame
df_combined['Puntuacion'] = df_combined.apply(calcular_puntuacion, axis=1, media_tweets=media_tweets)

# Mostrar el DataFrame con las puntuaciones
print(df_combined[['Jornada', 'Sentimiento Global', 'Numero de Tweets', 'Resultado', 'Posición', 'Distancia Descenso', 'Diferencia Posiciones', 'Racha', 'Puntuacion']])