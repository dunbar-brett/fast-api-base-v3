# Current App
from todo_app.db.connector import Base, SessionLocal, engine
from todo_app.models.item import Item
from todo_app.models.user import User


def recreate_and_seed():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # clear
        db.query(Item).delete()
        db.query(User).delete()
        db.commit()

        # create users
        u1 = User(name="Alice")
        u2 = User(name="Bob")
        db.add_all([u1, u2])
        db.commit()
        db.refresh(u1)
        db.refresh(u2)

        # create items
        items = [
            Item(title="Alice Task 1", description="Do laundry", user_id=u1.id),
            Item(title="Alice Task 2", description="Buy groceries", user_id=u1.id),
            Item(title="Alice Task 3", description="Read book", user_id=u1.id),
            Item(title="Bob Task 1", description="Pay bills", user_id=u2.id),
            Item(title="Bob Task 2", description="Call mom", user_id=u2.id),
            Item(title="Bob Task 3", description="Fix bike", user_id=u2.id),
        ]
        db.add_all(items)
        db.commit()
        print("Seeded DB with users and items")
    finally:
        db.close()


if __name__ == "__main__":
    recreate_and_seed()
