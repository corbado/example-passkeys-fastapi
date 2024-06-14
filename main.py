from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from corbado_python_sdk import Config, CorbadoSDK, UserEntity, SessionInterface

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

PROJECT_ID: str = os.getenv("PROJECT_ID", "pro-xxx")
API_SECRET: str = os.getenv("API_SECRET", "corbado1_xxx")

# Session config
short_session_cookie_name = "cbo_short_session"


# Config has a default values for 'short_session_cookie_name' and 'BACKEND_API'
config: Config = Config(
    api_secret=API_SECRET,
    project_id=PROJECT_ID,
)

# Initialize SDK
sdk: CorbadoSDK = CorbadoSDK(config=config)
sessions: SessionInterface = sdk.sessions


@app.get("/", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request, "PROJECT_ID": PROJECT_ID}
    )


@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    # Acquire cookies with your preferred method
    token: str = request.cookies.get(config.short_session_cookie_name) or ""
    user: UserEntity = sessions.get_current_user(short_session=token)

    if user.authenticated:
        context = {
            "request": request,
            "PROJECT_ID": PROJECT_ID,
            "USER_ID": user.user_id,
            "USER_NAME": user.name,
            "USER_EMAIL": user.email,
        }
        return templates.TemplateResponse("profile.html", context)

    else:
        return Response(content="You are not authenticated or have not yet confirmed your email.", status_code=401)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
