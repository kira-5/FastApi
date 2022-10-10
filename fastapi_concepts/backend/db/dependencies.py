from this import d
# from fastapi import FastAPI, Request, Response
from db.session import flask_sqlalchemy_connect
from typing import Generator

SessionLocal, alchemyEngine = flask_sqlalchemy_connect()


# Dependency injection
# db_session_middleware() : main.py

# def get_db(request: Request):
#     return request.state.db


# Dependency injection
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# https://www.fastapitutorial.com/blog/dependencies-in-fastapi/