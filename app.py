from flask import Flask, render_template, request, session, redirect, url_for
import os
import omdb
import spoonacular as sp
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

OMDB_API_KEY = os.environ.get("OMDB_API_KEY")
SPOONACULAR_API_KEY = os.environ.get("SPOONACULAR_API_KEY")
SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY

omdb.set_default('apikey', OMDB_API_KEY)
spoon = sp.API(SPOONACULAR_API_KEY)

class IngredientsForm(FlaskForm):
    ingredients = StringField("What's in your fridge?", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['POST', 'GET'])
def home():
    ingredients = None
    form = IngredientsForm()
    if form.validate_on_submit():
        ingredients = form.ingredients.data
        # form.ingredients.data = ''
        response = spoon.search_recipes_by_ingredients(ingredients)
        data = response.json()
        return str(data)
    return render_template('home.html', form=form, ingredients=ingredients)

@app.route('/movie/<movie>', methods=['POST', 'GET'])
def omdb_test(movie):
     r = omdb.search(movie)
     return str(r)

@app.route('/dish', methods=['POST', 'GET'])
def sp_test():
    r = spoon.detect_food_in_text('Spaghetti')
    data = r.json()
    return str(data)

@app.route('/ideas', methods=['POST', 'GET'])
def ideas():
    return render_template('ideas.html')

if __name__ == '__main__':
    app.run(debug=True)