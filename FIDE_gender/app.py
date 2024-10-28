from flask import Flask, render_template, request, Response
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from functions import *

app = Flask(__name__)

# Cargar los datos
ratings_dict = {}
for i in range(20, 21):
    year = "20" + str(i)
    ratings_dict[year] = pd.read_csv("./content/ratings_" + year + ".csv", sep=',')

players = pd.read_csv("./content/players.csv", sep=',')
countries = sorted(players['federation'].unique())

@app.route("/")
def home():
    return render_template("home.html")
# Ruta principal con formulario para seleccionar país y rango de años
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    selected_country = 'ESP'
    year_range = range(1999, 2007)
    number_topplayerss = 10
    plot_url = None

    if request.method == 'POST':
        selected_country = request.form.get('country')
        year_start = int(request.form.get('year_start'))
        year_end = int(request.form.get('year_end'))
        number_topplayerss = int(request.form.get('top_players'))
        year_range = range(year_start, year_end + 1)

        # Generar el gráfico
        plot_url = generate_plot(ratings_dict["2020"],players,selected_country, year_range, number_topplayerss)

    return render_template('plot.html', countries=countries, plot_url=plot_url, selected_country=selected_country, year_range=year_range)
@app.route('/world_map', methods=['GET', 'POST'])
def world_map():
    year_range = range(1999, 2005)
    number_topplayerss = 10
    plot_url = None

    if request.method == 'POST':
        # Obtener valores seleccionados del formulario
        year_start = int(request.form.get('year_start'))
        year_end = int(request.form.get('year_end'))
        number_topplayerss = int(request.form.get('top_players'))

        # Rango de años
        year_range = range(year_start, year_end + 1)
        
        # Llamar a la función que genera el gráfico con las opciones seleccionadas
        img = generate_mapamundi(ratings_dict["2020"], players, year_range, number_topplayerss)

        # Retornar el gráfico generado
        return Response(img, mimetype='image/png')

    # En caso de GET, mostrar el formulario con la lista de países
    countries = players['federation'].unique()  # Suponiendo que tienes esta lista de países
    return render_template('map.html', countries=countries)
@app.route("/table", methods=["GET", "POST"])
def table():
    table_html = None
    
    if request.method == "POST":
        year_start = int(request.form.get("year_start"))
        year_end = int(request.form.get("year_end"))
        year_range = range(year_start, year_end + 1)
        number_topplayerss = int(request.form.get("top_players"))

        # Generar la tabla
        table_html = generate_table(ratings_dict["2020"], players, year_range, number_topplayerss)

    return render_template("table.html", table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)