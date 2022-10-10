import time

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from db.session import flask_sqlalchemy_connect
from config.api_settings import settings
from users.router import user_api_router
from jobs.router import job_api_router
from db.base import Base
# from dotenv import load_dotenv
from pathlib import Path
from config.env_config import environment_config


env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

ENV, CONFIG = environment_config()

SessionLocal, alchemyEngine = flask_sqlalchemy_connect()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI(
    title=CONFIG.get(ENV, 'PROJECT_NAME'),
    version=CONFIG.get(ENV, 'PROJECT_VERSION'),
    docs_url=CONFIG.get(ENV, 'DOCS_URL'),
    redoc_url=CONFIG.get(ENV, 'REDOC_URL'),
    openapi_url=CONFIG.get(ENV, 'OPENAPI_URL'),
)


def register_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_router(app):
    app.include_router(user_api_router, prefix=settings.API_V1_STR)
    app.include_router(job_api_router, prefix=settings.API_V1_STR)


def create_tables(alchemyEngine):
    Base.metadata.create_all(bind=alchemyEngine)


def start_application(app):
    include_router(app)
    # configure_static(app)
    register_cors(app)
    create_tables(alchemyEngine)

    return app


fast_api = start_application(app)


# @fast_api.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)

#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()

#     return response


# Add process time as a header in api call
@fast_api.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
