import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

# Cargar el dataset
df = pd.read_csv('guede.csv')  # Cambia por el nombre de tu archivo

# Convertir la columna de fecha a formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# Inicializar el analizador de sentimientos VADER
analyzer = SentimentIntensityAnalyzer()

# Función para obtener el sentimiento de un tweet
def get_sentiment(text):
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores['compound']

# Aplicar la función de análisis de sentimientos a la columna de contenido
df['Sentiment'] = df['Content'].apply(get_sentiment)

# Extraer solo la fecha (sin hora) para agrupar por día
df['Date'] = df['Date'].dt.date

# Agrupar por día y calcular la media del sentimiento de los tweets
sentiment_per_day = df.groupby('Date')['Sentiment'].mean().reset_index()

# Mostrar el resultado
print(sentiment_per_day)

# Si quieres guardar los resultados en un archivo CSV:
sentiment_per_day.to_csv('sentiment_per_day.csv', index=False)