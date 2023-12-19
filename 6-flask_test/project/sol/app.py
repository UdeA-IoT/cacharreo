from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return """
            <h1>Adopt a Pet!</h1>
            <p>Browse through the links below to find
            your new furry friend:</p>
            <ul>
              <li> Dogs
              <li> Cats
              <li> Rabbits
            </ul>
          """

@app.route('/animals')
def animals():
  html = "<h1>List of pets</h1>"
  return html

if __name__ == '__main__':
    app.run()
