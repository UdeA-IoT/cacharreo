from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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

"""
@app.get("/")
async def home(response_class=HTMLResponse):
    with open(os.path.join("templates", 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")    
"""

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    puertos = ["COM1", "COM2", "COM3"]
    return templates.TemplateResponse("index.html", {"request": request, "puertos": puertos})
    

