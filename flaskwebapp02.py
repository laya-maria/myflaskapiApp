from flask import Flask, request, jsonify


app = Flask(__name__)


Data = [ 
    {"id": 1, "campus" : "MMC", 
       "lat": 25.76057810, "lon": -80.36934121},
    {"id": 2, "campus" : "BBC", 
        "lat": 25.90932603, "lon": -80.13842127}
]

next_id = 3

#week 10 : a route for status, aroute for all the items
#route for a specific item(thru an id)
#create a simple client to request data from API
@app.route('/')
def index():
    return"<h2>Welcome"