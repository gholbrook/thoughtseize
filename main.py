from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()


@app.get("/")
def home():
    return {"Hello World"}

@app.get("/metagame")
def metagame():
    return {"some text"}

@app.get("/tournaments")
def tournaments():
    return {"some text"}

@app.get("/archives")
def archives():
    return {"some text"}