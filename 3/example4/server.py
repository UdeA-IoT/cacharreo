from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from typing import Annotated
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

"""
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
"""
# https://code-maven.com/slides/python/fastapi-return-html-file
# https://gist.github.com/gbaldera/3751301
# https://jinja.palletsprojects.com/en/3.1.x/templates/
# https://fastapi.tiangolo.com/advanced/custom-response/
# https://stackoverflow.com/questions/74504161/how-to-submit-selected-value-from-html-dropdown-list-to-fastapi-backend
# https://opentechschool.github.io/python-flask/core/forms.html

# https://fastapi.tiangolo.com/tutorial/request-forms/ (Instalar)
# https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/

"""
@app.get("/")
async def home(response_class=HTMLResponse):
    with open(os.path.join("templates", 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")    
"""

@app.get('/')
def read_root():
    return 'Ensayo'

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    puertos = ["COM1", "COM2", "COM3"]
    return templates.TemplateResponse("index.html", {"request": request, "puertos": puertos})


@app.get("/control")
async def control(port: str):
    print(port)

    """
    app.serial = serial.Serial(port_id,9600)

    if app.serial == None:
        return {"Connection": "Fail"}
    else:
        return {"Connection": "Open", }
    """

"""

               value="{{ request.form['title'] }}"></input>


@app.get("/connect", response_class=HTMLResponse)
async def read_item(request: Request):
    puertos = ["COM1", "COM2", "COM3"]
    return templates.TemplateResponse("index.html", {"request": request, "puertos": puertos})


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
"""