from flask import Flask, render_template
from helper import recipes, descriptions, ingredients

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/recipe/<int:id>")
def recipe(id):
  #### Add template variables as
   
  #### variable assignment arguments
  return render_template("recipe.html", template_recipe = recipes[id], template_description = descriptions[id], template_ingredients = ingredients[id])
