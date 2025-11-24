# External Dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Current App
from todo_app.config import settings

# Using sync SQLAlchemy + psycopg2-binary for simplicity
engine = create_engine(settings.DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


# dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
