import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()
root_path = os.getenv("SCRIPT_NAME", "")

# Assign API, API title and version
app = FastAPI(root_path=root_path)
app.title = "Basic API with FastAPI"
app.version = "0.0.1"

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse, tags=['home'])
async def home(request: Request):
    return templates.TemplateResponse(name="home.html", request=request)


@app.get('/about', response_class=HTMLResponse, tags=['about'])
async def about(request: Request):
    return templates.TemplateResponse(name="about.html", request=request)
