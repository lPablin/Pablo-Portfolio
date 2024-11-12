import pandas as pd
import os

def corregir_nombres_equipos(df):
    """
    Corrige los nombres de los equipos en un DataFrame.

    Args:
        df: El DataFrame a corregir.

    Returns:
        El DataFrame con los nombres de los equipos corregidos.
    """
    correcciones = {
        'LeganÃ©s': 'Leganes',
        'AlcorcÃ³n': 'Alcorcon',
        'MÃ¡laga': 'Malaga',
        'MirandÃ©s': 'Mirandes',
        'AlmerÃ­a': 'Almeria',
        'Deportivo AlavÃ©s': 'Alaves'
    }
    for columna in df.columns:
        df[columna] = df[columna].replace(correcciones)
    return df

def corregir_excels_en_carpeta(carpeta):
    """
    Recorre todos los archivos Excel en una carpeta y corrige los nombres de los equipos.

    Args:
        carpeta: La ruta a la carpeta que contiene los archivos Excel.
    """
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.xlsx') or archivo.endswith('.xls'):
            ruta_archivo = os.path.join(carpeta, archivo)
            df = pd.read_excel(ruta_archivo)
            df_corregido = corregir_nombres_equipos(df)
            df_corregido.to_excel(ruta_archivo, index=False)

# Ejemplo de uso:
carpeta_excels = './resultados_hypermotion'  # Reemplaza con la ruta a tu carpeta
corregir_excels_en_carpeta(carpeta_excels)