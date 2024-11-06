import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Paso 1: Cargar y concatenar todos los archivos CSV

# Usamos glob para buscar todos los archivos CSV en la carpeta actual que sigan un patrón
# Cambia la ruta si tus archivos están en otro directorio

all_files=['joseba'+'_'+'Eibar','calleja'+'_'+'Levante','albes'+'_'+'Albacete','callejaoviedo'+'_'+'Real Oviedo','ziganda'+'_'+'Huesca','nafti'+'_'+'Levante','guede'+'_'+'Malaga','Cervera'+'_'+'Real Oviedo','delamo'+'_'+'FC Cartagena']

# Lista para almacenar los DataFrames
df_list = []

# Iterar sobre todos los archivos y cargarlos
for file in all_files:
    df = pd.read_csv(file+'_analisis_partidos.csv')
    df_list.append(df)

# Concatenar todos los DataFrames en uno solo
df_concatenado = pd.concat(df_list, ignore_index=True)

# Paso 2: Generar una matriz de correlación

# Convertir las columnas que sean categóricas a numéricas si es necesario
# Por ejemplo, si la columna 'Despedido' es categórica (0 o 1), no hace falta convertir
# Pero si hay otras columnas categóricas (como 'En Playoff'), puedes asegurarte que están en formato numérico

# Generar la matriz de correlación
correlation_matrix = df_concatenado.corr()

# Mostrar la matriz de correlación
print(correlation_matrix)

# Paso 3: Visualización opcional usando un heatmap

# Crear un heatmap de la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación")
plt.savefig('Matriz_correlacion.png', format='png')

plt.show()