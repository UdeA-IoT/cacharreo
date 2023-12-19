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

if __name__ == '__main__':
    app.run()
