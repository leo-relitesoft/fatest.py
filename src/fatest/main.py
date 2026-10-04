import os
from fastapi import FastAPI
from fatest.routes import users

api = FastAPI(title="Fatest API")

api.include_router(users.router)

@api.get("/db")
def root() -> str:
    db_url = os.getenv('DB_USERS_URL')
    return f"{db_url}"


