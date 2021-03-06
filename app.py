from flask import Flask, render_template
from swapi.swapi import BasicApi, create_planets

app = Flask(__name__)

SWAPI = BasicApi('SWAPI')
planet_data = SWAPI.get_all_pages()
all_planets = create_planets(planet_data)


@app.route("/")
def index():
    return render_template('index.html', planets=all_planets)


@app.route("/climate/<selected_climate>")
def view_by_climate(selected_climate):
    climate_planets = [planet for planet in all_planets if selected_climate in planet.climate]
    return render_template('index.html', planets=climate_planets)


@app.route("/terrain/<selected_terrain>")
def view_by_terrain(selected_terrain):
    terrain_planets = [planet for planet in all_planets if selected_terrain in planet.terrain]
    return render_template('index.html', planets=terrain_planets)


if __name__ == '__main__':
    app.run()
