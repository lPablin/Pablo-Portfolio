import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Suponiendo que tienes las fechas de los partidos en una lista

fechas_partidos = ["14 Aug", "21 Aug", "28 Aug", "4 Sep", "11 Sep", "18 Sep"]


import pandas as pd

año=2024
equipo_seleccionado= 'Huesca'
entrenador='ziganda'
anio = "2023"

equipo_seleccionado='Levante'
año='2023'
entrenador='nafti'
anio = "2022"  # Puedes cambiar el año si es necesario

entrenador='guede'
anio = "2022"
equipo_seleccionado='Malaga'
año='2023'

entrenador='Cervera'
anio = "2023"
equipo_seleccionado='Real Oviedo'
año='2024'


entrenador='delamo'
anio = "2023"
equipo_seleccionado='FC Cartagena'
año='2024'


entrenador='callejaoviedo'
anio = "2024"
equipo_seleccionado='Real Oviedo'
año='2025'



entrenador='albes'
anio = "2023"
equipo_seleccionado='Albacete'
año='2024'


entrenador='calleja'
anio = "2023"
equipo_seleccionado='Levante'
año='2024'


entrenador='joseba'
anio = "2023"
equipo_seleccionado='Eibar'
año='2024'


entrenador='bolo'
anio = "2022"
equipo_seleccionado='Real Oviedo'
año='2023'

meses_ingles = {
    'Ene': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Abr': 'Apr', 'May': 'May', 'Jun': 'Jun',
    'Jul': 'Jul', 'Ago': 'Aug', 'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dic': 'Dec'
}
info = pd.read_csv(str(equipo_seleccionado)+str(año)+'_analisis_partidos.csv')

# Extraer la parte de la fecha del string
info['Fecha_Limpia'] = info['Fecha'].str.extract(r'(\d{2} \w{3} \d{2})')
info['Fecha_Limpia'] = info['Fecha_Limpia'].replace(meses_ingles, regex=True)
info['Fecha_Limpia2'] = info['Fecha_Limpia'].str.slice(stop=6)
info['Fecha_Limpia'] = pd.to_datetime(info['Fecha_Limpia'], format='%d %b %y', errors='coerce')

# Crear una lista con todas las fechas extraídas
fechas_partidos = info['Fecha_Limpia'].tolist()
df = pd.read_csv(entrenador+'.csv')  # Cambia por el nombre de tu archivo
# Convertir la columna 'Date' de tu DataFrame a datetime

if anio=="2024":
    df['Date'] = df['Date'] + ', 2024'

df['Date'] = pd.to_datetime(df['Date'])
# Crear un DataFrame para almacenar los resultados
resultados = []
# Instanciar el analizador VADER
analyzer = SentimentIntensityAnalyzer()
# Función para calcular el sentimiento usando VADER
def get_sentiment_score(text):
        sentiment_scores = analyzer.polarity_scores(text)
        score = sentiment_scores['compound']
        # Definir palabras clave negativas
        negative_keywords = ['tomar por culo', 'vergonzoso','dimision', 'al paro', 'out', 'turrón','destitu','despedido','vete ya','echar a '+entrenador,'dimit',entrenador+' fuera']
    
        # Si encontramos palabras clave negativas y el puntaje es positivo, multiplicamos por -1
        if any(negative_word in text.lower() for negative_word in negative_keywords) and score > 0:
            print("Texto pasado a negativo")
            print(text)
            return score * -1  # Multiplicamos por -1
        return score  # Si no, devolvemos el puntaje original

# Clasificación de sentimientos
def classify_sentiment(score):
    if score > 0.1:
        return 'Positivo'
    elif score < -0.1:
        return 'Negativo'
    else:
        return 'Neutro'

pd.set_option('display.max_colwidth', None)

# Iterar sobre cada fecha de partido
for fecha in fechas_partidos:
    # Definir el rango de fechas (día anterior, día del partido, día posterior)
    rango_inicio = fecha
    rango_fin = fecha + pd.Timedelta(days=2)
    
    # Filtrar tweets que caen dentro de este rango de fechas
    tweets_partido = df[(df['Date'] >= rango_inicio) & (df['Date'] <= rango_fin)].copy()

    num_nan_before = tweets_partido['Cleaned_Content'].isna().sum()
    #print(f"Número de NaN antes del reemplazo: {num_nan_before}")
    tweets_partido.loc[:,'Cleaned_Content'] = tweets_partido['Cleaned_Content'].fillna('')

    if not tweets_partido.empty:
        # Calcular el análisis de sentimientos global usando la polaridad
        tweets_partido['Sentimiento'] = tweets_partido['Cleaned_Content'].apply(get_sentiment_score)
        # Clasificar el sentimiento de los tweets
        tweets_partido['Sentimiento_Clasificado'] = tweets_partido['Sentimiento'].apply(classify_sentiment)
        
        sentimiento_global = tweets_partido['Sentimiento'].mean()
        # Contar el número de tweets
        num_tweets = len(tweets_partido)

        # Calcular porcentajes directamente sin crear una nueva columna
        sentimiento_clasificado = tweets_partido['Sentimiento'].apply(classify_sentiment)

        # Calcular los porcentajes
        total_tweets = len(tweets_partido)
        positivos = len(sentimiento_clasificado[sentimiento_clasificado == 'Positivo'])
        neutros = len(sentimiento_clasificado[sentimiento_clasificado == 'Neutro'])
        negativos = len(sentimiento_clasificado[sentimiento_clasificado == 'Negativo'])
    
        porcentaje_positivos = (positivos / total_tweets) * 100
        porcentaje_neutros = (neutros / total_tweets) * 100
        porcentaje_negativos = (negativos / total_tweets) * 100
        # Almacenar los resultados
        resultados.append({
            'Partido': fecha.strftime('%d %b'),
            'Sentimiento Global': sentimiento_global,
            'Porcentaje positivos': porcentaje_positivos,
            'Porcentaje neutros': porcentaje_neutros,
            'Porcentaje negativos': porcentaje_negativos,
            'Numero de Tweets': num_tweets
        })
    
        # Filtrar tweets positivos
        tweets_positivos = tweets_partido[tweets_partido['Sentimiento_Clasificado'] == 'Positivo']
        if porcentaje_positivos>0:
            # Imprimir los tweets positivos
            print("Tweets Positivos:")
            print(tweets_positivos[['Cleaned_Content', 'Sentimiento']])  # Puedes mostrar solo las columnas que te interesan

# Convertir los resultados en un DataFrame
resultados_df = pd.DataFrame(resultados)
print(resultados_df)
columnas_a_incluir = ['Resultado',  'Posición'  ,'Distancia Descenso',  'En Descenso',  'En Playoff',  'Diferencia Posiciones',  'Racha']
df_info = info[columnas_a_incluir]
df_concatenado = pd.concat([resultados_df, df_info], axis=1)
# Crear la nueva columna
nueva_columna = [0] * len(df_concatenado)

# Asignar 1 a la última fila
#nueva_columna[-1] = 1

# Añadir la columna al DataFrame
df_concatenado['Despedido'] = nueva_columna
# Mostrar los resultados
print(df_concatenado)

# Opcional: Guardar en un archivo CSV
df_concatenado.to_csv(entrenador+'_'+equipo_seleccionado+'_analisis_partidos.csv', index=False)