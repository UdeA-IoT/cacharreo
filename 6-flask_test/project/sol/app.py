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
  """
  html = "<h1>List of "+ pet_type +"</h1>\n"
  html += "<ul>\n"
  for pet in pets[pet_type]:
    item = "<li>" + pet['name'] + "\n"
    html += item
  html += "</ul>"
  return html
  """
  html = "<h1>List of " + pet_type + "</h1>\n"
  html += "<ul>\n"
  for idx, item in enumerate(pets[pet_type]):
    link = "/animals/" + pet_type + "/" + str(idx)
    link = "href=\"" + link + "\""
    item = "<li> <a " + link + "> " + pets[pet_type][idx]['name'] + " </a> </li>\n"
    html += item
  html += "</ul>\n"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return "<h1>" + pet['name'] + "</h1>" + \
         "<img src= \"" + pets[pet_type][pet_id]['url'] + "\">" + \
         "<p>" + pets[pet_type][pet_id]['description'] + "</p>" + \
         "<ul>" + \
         "<li>" +  pets[pet_type][pet_id]['breed'] + "</li>" + \
         "<li>" +  str(pets[pet_type][pet_id]['age']) + "</li>" + \
         "</ul>"

if __name__ == '__main__':
    app.run()
