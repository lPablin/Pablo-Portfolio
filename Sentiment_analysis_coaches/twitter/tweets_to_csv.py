import pandas as pd
import re

def process_tweets(filename):
    # Leer el contenido del archivo de texto
    with open(filename + '.txt', 'r', encoding='utf-8') as file:
        tweets = file.read()

    # Expresión regular para identificar los delimitadores de tweets
    split_pattern = re.compile(
        r'(@[^\n]+)\n·\n([^\n]+)\n', re.MULTILINE
    )

    # Dividir el texto en tweets usando el patrón
    tweet_sections = split_pattern.split(tweets)

    # Lista para almacenar los datos procesados
    tweet_data = []

    # Procesar las secciones divididas
    for i in range(1, len(tweet_sections), 3):
        username = tweet_sections[i].strip()
        date = tweet_sections[i + 1].strip()
        content = tweet_sections[i + 2].strip()
        
        # Corregir el contenido si es el último tweet
        if i + 3 < len(tweet_sections):
            next_username = tweet_sections[i + 3].strip()
            if not next_username.startswith('@'):
                content += ' ' + tweet_sections[i + 3].strip()
        
        # Añadir la información a la lista
        tweet_data.append([username, date, content])

    # Crear un DataFrame con los datos extraídos
    df = pd.DataFrame(tweet_data, columns=['Username', 'Date', 'Content'])

    # Mostrar el DataFrame limpio
    print(df)

    # Guardar en un archivo CSV
    df.to_csv(filename + '.csv', index=False)

# Ejemplo de uso
# Para procesar varios archivos puedes llamar a la función con diferentes nombres de archivo
nombre="ziganda_jornada"
for i in range(1,10+1):
    process_tweets(nombre+str(i))