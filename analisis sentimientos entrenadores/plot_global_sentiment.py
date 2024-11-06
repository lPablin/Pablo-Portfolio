import pandas as pd
import matplotlib.pyplot as plt


fig, ax1 = plt.subplots(figsize=(10, 6))

# Eje Y izquierdo - Sentimiento Global
ax1.set_xlabel('Fecha del Partido')
ax1.set_ylabel('Sentimiento Global', color='tab:blue')

ax1.tick_params(axis='y', labelcolor='tab:blue')

# Eje Y derecho - Resultado/Racha
ax2 = ax1.twinx()
ax2.set_ylabel('Racha', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Título del gráfico
plt.title('Sentimiento Global y Racha por Partido')

# Formato de la fecha en el eje X
fig.autofmt_xdate()
all_files=['joseba'+'_'+'Eibar','calleja'+'_'+'Levante','albes'+'_'+'Albacete','callejaoviedo'+'_'+'Real Oviedo']
all_files=['ziganda'+'_'+'Huesca','nafti'+'_'+'Levante','guede'+'_'+'Malaga','Cervera'+'_'+'Real Oviedo','delamo'+'_'+'FC Cartagena']
all_files=['Cervera'+'_'+'Real Oviedo','callejaoviedo'+'_'+'Real Oviedo','Bolo_Real Oviedo']
# Lista para almacenar los DataFrames
df_list = []

# Iterar sobre todos los archivos y cargarlos
for file in all_files:
    df = pd.read_csv(file+'_analisis_partidos.csv')
    df_list.append(df)
    # Paso 2: Convertir las fechas de los partidos en formato datetime
    df['Partido'] = pd.to_datetime(df['Partido'], format='%d %b')
    # Paso 3: Crear un gráfico con dos ejes Y (sentimiento y resultado/racha)
     # Obtener el nombre del equipo (o una etiqueta personalizada)
    equipo = file.split('_')[0]  # Asume que el nombre del equipo está al inicio del archivo
    
    # Paso 3: Graficar el Sentimiento Global en el eje izquierdo (ax1)
    ax1.plot(df['Partido'], df['Sentimiento Global'], marker='o', label=f'Sentimiento {equipo}')
    
    # Paso 4: Graficar la Racha en el eje derecho (ax2)
    ax2.plot(df['Partido'], df['Numero de Tweets'], marker='s', label=f'Numero de Tweets {equipo}')

# Configuraciones adicionales
ax1.set_xlabel('Fecha del Partido')
ax1.set_ylabel('Sentimiento Global', color='tab:blue')
ax2.set_ylabel('Racha', color='tab:red')

# Leyenda separada para el eje izquierdo (Sentimiento Global)
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 1))

# Leyenda separada para el eje derecho (Racha)
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1))

# Mostrar el gráfico
plt.show()