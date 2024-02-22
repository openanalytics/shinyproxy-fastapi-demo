from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from models import Gender, Role, User
# from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
# import os

# Assign API, API title and version
app = FastAPI()
app.title = "Basic API with FastAPI"
app.version = "0.0.1"




db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse, tags=['home'])
async def message(request: Request):
    return templates.TemplateResponse(name="htmlTemplate.html", request=request)


@app.get('/users/{gender}', tags=['db'])
async def get_users_by_gender(gender: Gender):
    out = []
    for item in db:
        if item.gender == gender:
            out.append(item)
    return out


@app.get("/api/v1/users", tags=['db'])
async def get_users():
    return db


@app.post("/api/v1/users", tags=['db'])
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{id}", tags=['db'])
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )
