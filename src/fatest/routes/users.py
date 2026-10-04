import email_validator
from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, EmailStr


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


class ApiResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
        str_strip_whitespace=True,
    )

class UserDetails(ApiResponse):
    username: str = "john"
    user_id: int
    email: EmailStr = "none@x.com"


@router.get("/")
def get_users() -> list[dict[str, str]]:
    return [{"username": "john"}, {"username": "rick"}]

@router.get("/{user_id}")
def get_user(user_id: int) -> UserDetails:
    return UserDetails(**{"user_id": user_id})

