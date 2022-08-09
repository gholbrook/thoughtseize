from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request})


@app.get("/")
def home():
    return {"Hello World"}

@app.get("/metagame")
async def metagame():
    return {"some text"}

@app.get("/tournaments")
async def tournaments():
    return {"some text"}

@app.get("/archives")
async def archives():
    return {"some text"}

