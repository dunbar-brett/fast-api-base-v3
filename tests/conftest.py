# External Dependencies
import pytest
from fastapi.testclient import TestClient

# Current App
from todo_app.db.connector import Base, SessionLocal, engine
from todo_app.main import app
from todo_app.models.item import Item
from todo_app.models.user import User


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def test_user():
    """Create a single user for the test session and return its id.

    Tests can depend on `test_user` to get the numeric id instead of hardcoding.
    """
    session = SessionLocal()
    try:
        user = User(name="Chuck")
        session.add(user)
        session.commit()
        session.refresh(user)
        item = Item(title="Alice Task 1", description="Do laundry", user_id=user.id)
        session.add(item)
        session.commit()
        session.refresh(user)
        yield user.id
    finally:
        session.close()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
