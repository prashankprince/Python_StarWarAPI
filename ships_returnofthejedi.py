# -*- coding: utf-8 -*-
"""Ships_ReturnoftheJedi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TNs3Q2JF6bIuYzYXvy-U97EsZPKklghU
"""

import requests

#go to starship API
url = "https://swapi.dev/api/starships/"


#get json data
json_data = requests.get(url).json()

#and check which has "films": "https://swapi.dev/api/films/3/" 
# which means from movie named 'Return of the Jedi'
#and get all ship names

for ship in json_data['results']:
  films = ship['films']
  #print(ship['films'])
  for x in range(len(films)):
    if films[x] == 'https://swapi.dev/api/films/3/':
      print(ship['name'])