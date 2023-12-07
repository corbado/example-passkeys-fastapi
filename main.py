from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

PROJECT_ID = os.getenv("PROJECT_ID", "pro-xxx")

@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "PROJECT_ID": PROJECT_ID})


@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request, "PROJECT_ID": PROJECT_ID})


@app.get("/{path}", response_class=HTMLResponse)
async def redirect_to_login(path: str):
    return RedirectResponse(url="/login")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)