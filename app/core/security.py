from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from schemas import user, role

User = user.User
Role = role.Role

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    if token == "admin-token":
        return User(username="admin_user", role=Role.ADMIN)
    elif token == "editor-token":
        return User(username="editor_user", role=Role.EDITOR)
    elif token == "viewer-token":
        return User(username="viewer_user", role=Role.VIEWER)
    else:
        raise HTTPException(status_code=401, detail="Invalid token")


def role_required(required_roles: list[Role]):
    def wrapper(user: User = Depends(get_current_user)):
        if user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied for role: {user.role}"
            )
        return user
    return wrapper
