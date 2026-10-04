from fastapi import FastAPI
from fatest.routes import users

api = FastAPI(title="Fatest API")

api.include_router(users.router)

@api.get("/")
def root() -> str:
    return f"{__name__}"

