from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from lib import Lib
from models import User

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "templates"),
    name="templates",
)

lib = Lib()

templates = Jinja2Templates(f"{Path(__file__).parent.absolute()}/templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register")
def register(new_user: User):
    print(new_user)
    response = lib.register_user(new_user)
    return JSONResponse(content=response, status_code=response["status_code"])
