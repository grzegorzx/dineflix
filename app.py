from flask import Flask
import os
import omdb
import spoonacular as sp

app = Flask(__name__)

OMDB_API_KEY = os.environ.get("OMDB_API_KEY")
SPOONACULAR_API_KEY = os.environ.get("SPOONACULAR_API_KEY")

omdb.set_default('apikey', OMDB_API_KEY)
spoon = sp.API(SPOONACULAR_API_KEY)



@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/office', methods=['POST', 'GET'])
def omdb_test():
     r = omdb.search('office')
     return str(r)

@app.route('/dish', methods=['POST', 'GET'])
def sp_test():
    r = spoon.detect_food_in_text('Spaghetti')
    data = r.json()
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)