import pandas as pd
año=2025
numjornadas=6
jornadas=[]
equipo_seleccionado= 'Real Oviedo'

posicion_anterior = 6

for i in range(1,numjornadas+1):
    jornada1 = pd.read_excel('./resultados_hypermotion/'+str(año)+'-jornada'+str(i)+'.xlsx')
    jornadas.append(jornada1)

clasificaciones=[]

for i in range(1,numjornadas+1):
    clasificacion1 = pd.read_excel('./resultados_hypermotion/'+str(año)+'-jornada'+str(i)+'-clasificacion.xlsx')
    clasificaciones.append(clasificacion1)

equipo_df = pd.DataFrame(columns=[
    'Jornada', 'Fecha', 'Resultado', 'Posición', 'Distancia Descenso',
    'En Descenso', 'En Playoff', 'Diferencia Posiciones', 'Racha'
])

for i, (jornada, clasificacion) in enumerate(zip(jornadas, clasificaciones)):
    numero_jornada = i + 1
    
    # Buscar el equipo en la jornada actual (local o visitante)
    if equipo_seleccionado in jornada['Equipo Local'].values:
        print("a")
        partido = jornada[jornada['Equipo Local'] == equipo_seleccionado].iloc[0]
        resultado = partido['Goles Local'] - partido['Goles Visitante']
        fecha_partido = partido['Fecha']
    elif equipo_seleccionado in jornada['Equipo Visitante'].values:
        print("a")
        partido = jornada[jornada['Equipo Visitante'] == equipo_seleccionado].iloc[0]
        resultado = partido['Goles Visitante'] - partido['Goles Local']
        fecha_partido = partido['Fecha']
    else:
        print("b")
        continue  # Si el equipo no jugó en esta jornada, se omite

    # Obtener la posición del equipo en la clasificación
    posicion_actual = clasificacion[clasificacion['Equipo'] == equipo_seleccionado]['Posición'].values[0]
    
    # Calcular la distancia al descenso
    posiciones_descenso = clasificacion.iloc[-4:]['Posición'].values
    distancia_descenso = min(posiciones_descenso) - posicion_actual
    
    # Determinar si está en descenso o en playoff
    en_descenso = 1 if distancia_descenso <= 0 else 0
    en_playoff = 1 if 3 <= posicion_actual <= 6 else 0
    
    # Calcular la diferencia de posiciones respecto al año anterior
    diferencia_posiciones = posicion_anterior - posicion_actual
    
    # Calcular la racha (puntos en las últimas 4 jornadas)
    if numero_jornada >= 4:
        racha = equipo_df.iloc[-4:]['Resultado'].apply(lambda x: 3 if x > 0 else (1 if x == 0 else 0)).sum()
    else:
        racha = equipo_df['Resultado'].apply(lambda x: 3 if x > 0 else (1 if x == 0 else 0)).sum()
    
    # Añadir la información al DataFrame
    equipo_df = equipo_df.append({
        'Jornada': numero_jornada,
        'Fecha': fecha_partido,
        'Resultado': resultado,
        'Posición': posicion_actual,
        'Distancia Descenso': distancia_descenso,
        'En Descenso': en_descenso,
        'En Playoff': en_playoff,
        'Diferencia Posiciones': diferencia_posiciones,
        'Racha': racha
    }, ignore_index=True)
print(equipo_df)
equipo_df.to_csv(str(equipo_seleccionado)+str(año)+'_analisis_partidos.csv', index=False)
  