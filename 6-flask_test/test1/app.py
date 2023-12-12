from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/reporter')
def reporter():
    return 'Reporter Bio'

if __name__ == '__main__':
    app.run()
