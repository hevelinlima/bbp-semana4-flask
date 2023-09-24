from flask import Flask, render_template
import json
import urllib.request
import certifi

##O certifi e a mudança dentro da variável response foram necessários para contornar um erro, sem eles o código retornava um erro de certificação ssl.

app = Flask(__name__)


# Endpoint: characters
@app.route("/")
def get_list_characters_page():
    url = "http://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("characters.html", characters=dicionario["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "http://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("profile.html", profile=dicionario)


@app.route("/lista")
def get_list_characters():
    url = "http://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    characters = response.read()
    dicionario = json.loads(characters)

    characters = []

    for character_in_dic in dicionario["results"]:
        character = {
            "name": character_in_dic["name"],
            "status": character_in_dic["status"],
            "id": character_in_dic["id"],
        }

        characters.append(character)

    return {"characters": characters}


# Endpoint: locations
@app.route("/locations")
def get_list_locations_page():
    url = "http://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("locations.html", locations=dicionario["results"])


@app.route("/location/<id>")
def get_location(id):
    url = "http://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("location.html", location=dicionario)


# Endpoint: episodes
@app.route("/episodes")
def get_list_episodes_page():
    url = "http://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("episodes.html", episodes=dicionario["results"])


@app.route("/episode/<id>")
def get_episode(id):
    url = "http://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url, cafile=certifi.where())
    data = response.read()
    dicionario = json.loads(data)

    return render_template("episode.html", episode=dicionario)


"""
@app.route("/location/lista")
def get_list_locations():
    url = "http://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url, cafile=certifi.where())
    locations = response.read()
    dicionario = json.loads(locations)
    locations = []
    for location_in_dic in dicionario["results"]:
        location = {
            "name": location_in_dic["name"],
            "type": location_in_dic["type"],
            "dimension": location_in_dic["dimension"],
            "url": location_in_dic["url"],
        }
        locations.append(location)
    return {"locations": locations}
"""
