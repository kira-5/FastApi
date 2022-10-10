from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse
from config.env_config import environment_config
import sys
import psycopg2 as ps


ENV, CONFIG = environment_config()
ps_database = CONFIG.get(ENV, 'database')
ps_user = CONFIG.get(ENV, 'user')
ps_password = CONFIG.get(ENV, 'password')
ps_host = CONFIG.get(ENV, 'host')
ps_port = CONFIG.get(ENV, 'port')


def postgres_connect():
    dbConnection = None
    try:
        print('Connecting to the PostgreSQL database...')
        dbConnection = ps.connect(
            database=ps_database,
            user=ps_user,
            password=ps_password,
            host=ps_host,
            port=ps_port)
        print("Connection Successful!")
    except (ps.DatabaseError) as error:
        print(error)
        sys.exit(1)

    return dbConnection


def flask_sqlalchemy_connect():
    alchemyEngine = None
    # Escaping Special Characters such as @ signs in Passwords¶
    password = urllib.parse.quote_plus(ps_password)
    # ps_url = f"postgresql+psycopg2://{ps_user}:password@{ps_host}: \
    # {ps_port}/{ps_database}?password={ps_password}"
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{ps_user}:{password}@{ps_host}:{ps_port}/{ps_database}"
    try:
        alchemyEngine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            pool_recycle=3600
        )
        # dbConnection_sql = alchemyEngine.connect()
    except (ps.DatabaseError) as error:
        print(error)
        sys.exit(1)

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=alchemyEngine
    )

    # return dbConnection_sql
    return SessionLocal, alchemyEngine
