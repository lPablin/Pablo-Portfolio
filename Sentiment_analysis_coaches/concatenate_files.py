import pandas as pd
nombre='callejaoviedo'
archivos=[]
for i in range(1,7):
    archivos.append(nombre+'_jornada'+str(i)+'.csv')

# Lista para almacenar los DataFrames
dfs = []
# Función para limpiar cada tweet
import re

# Función para limpiar el texto manteniendo las tildes y la ñ, y eliminando la última línea
def clean_tweet(text):
    # Eliminar menciones
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    # Eliminar URLs
    text = re.sub(r'http\S+', '', text)
    # Eliminar caracteres especiales excepto letras con acento, la ñ y espacios
    text = re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', text)
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar espacios extras
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Función para eliminar la última línea de cada celda
def remove_last_line(text):
    if '\n' in text:
        # Dividir el texto por líneas y eliminar la última
        lines = text.strip().split('\n')
        return '\n'.join(lines[:-1]).strip()
    return text

# Función para eliminar tweets que empiezan por "Replying to" o "Replying to and"
def remove_replying_tweets(text):
    # Convertir el texto a minúsculas para que la búsqueda no dependa de mayúsculas/minúsculas
    # Patrón para encontrar "Replying to" o "Replying to and" al inicio del texto
    reply_pattern = r'^replying to( and)?\s*'
    # Eliminar el patrón y retornar el contenido restante
    return re.sub(reply_pattern, '', text, flags=re.IGNORECASE).strip()

# Leer cada archivo y agregarlo a la lista de DataFrames
for archivo in archivos:
    data = pd.read_csv(archivo)  # Cambia a read_csv si son archivos CSV
    data['Cleaned_Content'] = data['Content'].apply(remove_last_line).apply(clean_tweet).apply(remove_last_line).apply(remove_replying_tweets).dropna().apply(clean_tweet)
    dfs.append(data)

# Concatenar todos los DataFrames
df_concatenado = pd.concat(dfs, ignore_index=True)
#df_concatenado = df_concatenado[df_concatenado['Date'] != 'Aug 23']

print(df_concatenado['Date'].unique())
# Guardar el DataFrame concatenado en un nuevo archivo Excel o CSV
#df_concatenado.to_excel('resultados_concatenados.xlsx', index=False)  # Guardar como Excel
df_concatenado.to_csv(nombre+'.csv', index=False)
print("Archivo guardado como .csv")
