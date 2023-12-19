from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return """
            <h1>Adopt a Pet!</h1>
            <p>Browse through the links below to find
            your new furry friend:</p>
            <ul>
              <li> <a href="/animals/dogs"> Dogs </a>
              <li> <a href="/animals/cats"> Cats </a>
              <li> <a href="/animals/rabbits"> Rabbits </a>
            </ul>
          """

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = "<h1>List of "+ pet_type +"</h1>\n"
  html += "<ul>\n"
  for pet in pets[pet_type]:
    item = "<li>" + pet['name'] + "\n"
    html += item
  html += "</ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return "<h1>" + pet['name'] + "</h1>"

if __name__ == '__main__':
    app.run()
