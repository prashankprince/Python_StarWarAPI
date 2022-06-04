# -*- coding: utf-8 -*-
"""Ships_Hyperdriverating.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SywRQAN4XatFEwFjyF9QtMYcGdlU8k12
"""

import requests

#go to starship API
url = "https://swapi.dev/api/starships/"


#get json data
json_data = requests.get(url).json()

# use try catch block for any value error and 
# check if hyperdrive_rating >=1.0 
# and print ship name

for ship in json_data['results']:
  hyperdrive_rating = ship['hyperdrive_rating']
  #print(ship['hyperdrive_rating'])
  try:
    if (float(hyperdrive_rating) >= float(1.0)): print(ship['name'])
  except ValueError:
    print('Error')