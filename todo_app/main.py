# External Dependencies
from fastapi import FastAPI

# Current App
from todo_app.api import items as items_router

app = FastAPI(title="Base API")
app.include_router(items_router.router, prefix="/api")
