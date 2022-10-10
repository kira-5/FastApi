
from db.dependencies import get_db
from config.env_config import environment_config
from db.base import Base
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse
import sys
import os
from config.api_settings import settings
from users.router import user_api_router
from jobs.router import job_api_router
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py


def start_application():
    app = FastAPI()
    app.include_router(user_api_router, prefix=settings.API_V1_STR)
    app.include_router(job_api_router, prefix=settings.API_V1_STR)
    return app


ENV, CONFIG = environment_config()
# ps_database = CONFIG.get(ENV, 'database')
ps_database = 'test'
ps_user = CONFIG.get(ENV, 'user')
ps_password = CONFIG.get(ENV, 'password')
ps_host = CONFIG.get(ENV, 'host')
ps_port = CONFIG.get(ENV, 'port')
password = urllib.parse.quote_plus(ps_password)
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{ps_user}:{password}@{ps_host}:{ps_port}/{ps_database}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=3600
)
SessionTesting = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
# Done, now type pytest in the terminal/cmd and see the magic !
