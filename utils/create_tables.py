# Current App
from todo_app.db.connector import Base, engine


def main():
    """
    Script to create all tables in the DB.
    Run: poetry run python create_tables.py
    """
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")


if __name__ == "__main__":
    main()
