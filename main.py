from typing import List
from corbado_python_sdk.entities.session_validation_result import (
    SessionValidationResult,
)
from corbado_python_sdk.generated.models.identifier import Identifier

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from corbado_python_sdk import (
    Config,
    CorbadoSDK,
)
from corbado_python_sdk import SessionService, IdentifierService, UserService


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
sessions: SessionService = sdk.sessions
identifiers: IdentifierService = sdk.identifiers


@app.get("/", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request, "PROJECT_ID": PROJECT_ID}
    )


@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    # Acquire cookies with your preferred method
    token: str = request.cookies.get(config.short_session_cookie_name) or ""
    validation_result: SessionValidationResult = (
        sessions.get_and_validate_short_session_value(short_session=token)
    )
    if validation_result.authenticated:

        emailList: List[Identifier] = identifiers.list_all_emails_by_user_id(
            user_id=validation_result.user_id
            or ""  # at this point user_id should be non empty string since user was authenticated
        )

        context = {
            "request": request,
            "PROJECT_ID": PROJECT_ID,
            "USER_ID": validation_result.user_id,
            "USER_NAME": validation_result.full_name,
            "USER_EMAIL": emailList[0].value,
        }
        return templates.TemplateResponse("profile.html", context)

    else:
        return Response(
            content="You are not authenticated or have not yet confirmed your email.",
            status_code=401,
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
