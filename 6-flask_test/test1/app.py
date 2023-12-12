from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():  # put application's code here
    # return 'Hello World!'
    return '<h1>Hello World!</h1>'

@app.route('/reporter')
def reporter():
    # return 'Reporter Bio'
    # return '<h2>Reporter Bio</h2>'
    return '''
        <h2>Reporter Bio</h2>
        <a href="/">Return to home page</a>
        '''

if __name__ == '__main__':
    app.run()
