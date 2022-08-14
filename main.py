from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

database = {}
database2 = {}
database3 = {}
for indexnum in range(10):
    database[f'Modern-Article-{indexnum}'] = dict(Author=f"Reid Duke", Format=f"Modern")
    database2[f'Standard-Article-{indexnum}'] = dict(Author=f"Ari Lax", Format=f"Standard")
    database3[f'Legacy-Article-{indexnum}'] = dict(Author=f"Gene Simmons", Format=f"Legacy")
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.get("/metagame")
async def metagame():
    return {"some text"}

@app.get("/tournaments")
async def tournaments():
    return {"some text"}

@app.get("/archives/articles")
async def archives(request: Request):
    return database,database2,database3

@app.get("/archives/articles/modern")
async def archives(request: Request):
    return database

@app.get("/archives/articles/standard")
async def archives(request: Request):
    return database2

@app.get("/archives/articles/legacy")
async def archives(request: Request):
    return database3

@app.get("/archives/articles{format_id}") #ex. want output "/archives/articles?format=modern" to return database
async def read_item(format_id):