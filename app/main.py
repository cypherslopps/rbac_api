from fastapi import FastAPI, Depends
from schemas.user import User, Role
from core.security import role_required

app = FastAPI()


@app.get("/admin/dashboard")
def admin_dashboard(user: User = Depends(role_required([Role.ADMIN]))):
    return {"message": f"Welcome to admin dashboard, {user.username}"}


@app.get("/editor/section")
def editor_section(user: User = Depends(role_required([Role.ADMIN, Role.EDITOR]))):
    return {"message": f"Welcome editor {user.username}"}
