from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import local

SQLALCHEMY_DATABASE_URL = f"postgresql://{local.DB_USER}:{local.DB_PASSWORD}@{local.DB_HOST}:{local.DB_PORT}/{local.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
