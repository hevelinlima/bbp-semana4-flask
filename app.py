from flask import Flask, render_template
import json
import urllib.request
import certifi

##O certifi e a mudança dentro da variável response foram necessários para contornar um erro, sem eles o código retornava um erro de certificação ssl.

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
  url = "http://rickandmortyapi.com/api/character"
  response = urllib.request.urlopen(url,cafile=certifi.where())
  data = response.read()
  dicionario = json.loads(data)

  return render_template("characters.html", characters=dicionario["results"])

@app.route("/profile/<id>")
def get_profile(id):
  url = "http://rickandmortyapi.com/api/character/" + id
  response = urllib.request.urlopen(url,cafile=certifi.where())
  data = response.read()
  dicionario = json.loads(data)

  return render_template("profile.html", profile=dicionario)

@app.route("/lista")
def get_list_characters():

  url = "http://rickandmortyapi.com/api/character"
  response = urllib.request.urlopen(url,cafile=certifi.where())
  characters = response.read()
  dicionario = json.loads(characters)

  characters = []

  for character_in_dic in dicionario["results"]:
    character = {
      "name": character_in_dic["name"],
      "status": character_in_dic["status"],
      "id": character_in_dic["id"]
    }

    characters.append(character)
  
  return {"characters":characters}
