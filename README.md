# Pablo-Portfolio
Data Science portfolio

# Portafolio de Proyectos

¡Bienvenido a mi portafolio de proyectos! Soy [Tu Nombre], un [profesión o rol] apasionado por [temas de interés, como ciencia de datos, desarrollo web, etc.]. Aquí puedes encontrar algunos de los proyectos en los que he estado trabajando.

## Proyectos Destacados

1. [**Chess Gender Comparison API**](https://github.com/tu-usuario/chess-gender-comparison-api)  
   Comparación del rendimiento ajedrecístico masculino y femenino a nivel mundial utilizando datos de la FIDE.  
   Tecnologías: Python, Flask, GeoPandas.

2. [**Proyecto 2**](https://github.com/tu-usuario/proyecto-2)  
   Breve descripción del segundo proyecto.
   
3. [**Proyecto 3**](https://github.com/tu-usuario/proyecto-3)  
   Breve descripción del tercer proyecto.

## Contacto

- [LinkedIn](https://linkedin.com/in/tu-usuario)
- [Correo electrónico](mailto:tu-email@gmail.com)

# Chess Gender Comparison API

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar y comparar el nivel ajedrecístico masculino y femenino en los distintos países del mundo. La comparación se realiza utilizando datos de jugadores de élite de la FIDE (Federación Internacional de Ajedrez), permitiendo obtener estadísticas detalladas sobre la presencia de jugadores y jugadoras en el ajedrez profesional.

El proyecto incluye una **API** que permite consultar estos datos de manera flexible, proporcionando información valiosa sobre el desempeño de los jugadores de élite en varios países y su distribución por género.

### Características principales:

- **Comparación de jugadores de élite**: El proyecto compara el número de jugadores y jugadoras de élite (los mejores jugadores de cada país) a nivel mundial.
- **Análisis de tendencias por país**: Visualización y análisis de los países con más presencia de jugadores en los rankings internacionales, tanto en categorías masculinas como femeninas.
- **Visualización en mapas interactivos**: Muestra un mapa interactivo que permite ver el rendimiento ajedrecístico de los distintos países y su balance de género.

## Funcionalidades de la API

La API desarrollada permite realizar diversas consultas para analizar el nivel ajedrecístico masculino y femenino. Algunas de sus funcionalidades incluyen:

1. **Consulta de jugadores por país**: Obtén información detallada de los jugadores de un país específico, su ranking y la proporción de hombres y mujeres.
   
   **Endpoint**: `/api/players/<country_code>`
   
   **Método**: `GET`

   **Descripción**: Devuelve el número de jugadores de élite y su distribución de género para el país con el código ISO dado.
   
   **Ejemplo de uso**:
   ```bash
   GET /api/players/USA
