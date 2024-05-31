from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import requests
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

PROJECT_ID = os.getenv("PROJECT_ID", "pro-xxx")
API_SECRET = os.getenv("API_SECRET", "corbado1_xxx")

# Session config
short_session_cookie_name = "cbo_short_session"
issuer = f"https://{PROJECT_ID}.frontendapi.corbado.io"
jwks_uri = f"https://{PROJECT_ID}.frontendapi.corbado.io/.well-known/jwks"

# Retrieve jwt public key
response = requests.get(jwks_uri)
response.raise_for_status()

jwks = response.json()
public_key = jwks["keys"][0]


@app.get("/", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "PROJECT_ID": PROJECT_ID})


@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    token = request.cookies.get(short_session_cookie_name)

    try:
        if not token:
            raise ValueError("No token found")

        payload = jwt.decode(
            token,
            key=public_key,
            algorithms=["RS256"],
            audience=API_SECRET,
            issuer=issuer,
        )

        if payload["iss"] != issuer:
            raise ValueError("Invalid issuer")

        context = {
            'request': request,
            'PROJECT_ID': PROJECT_ID,
            'USER_ID': payload["sub"],
            'USER_NAME': payload.get("name"),
            'USER_EMAIL': payload.get("email"),
        }

        return templates.TemplateResponse("profile.html", context)

    except Exception as e:
        print(e)
        return RedirectResponse(url="/login")


@app.get("/{path}", response_class=HTMLResponse)
async def redirect_to_login(path: str):
    return RedirectResponse(url="/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
