from pydantic import BaseModel
from .role import Role


class User(BaseModel):
    username: str
    role: Role
