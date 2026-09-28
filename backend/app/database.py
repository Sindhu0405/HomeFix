from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./homefix.db"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()


database_url = settings.database_url

# Render/PostgreSQL may provide a URL starting with postgres://
# SQLAlchemy uses postgresql://
if database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://",
        "postgresql://",
        1
    )

connect_args = {}

if database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}


engine = create_engine(
    database_url,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()