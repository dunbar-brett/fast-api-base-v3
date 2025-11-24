# External Dependencies
import pytest
from fastapi.testclient import TestClient

# Current App
from todo_app.db.connector import Base, SessionLocal, engine
from todo_app.main import app
from todo_app.models.user import User


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    # seed a user
    session = SessionLocal()
    u = User(name="Chuck")
    session.add(u)
    session.commit()
    session.close()
    yield
    # Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
