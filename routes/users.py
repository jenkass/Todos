from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])

users = {}


@user_router.post("/signup")
async def signup(data: User):
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this email")
    users[data.email] = data
    return {"message": "User successfully registered!"}


@user_router.post("/signin")
async def signin(user: UserSignIn):
    if not users.get(user.email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User doesn't exist!")
    if users[user.email].password != user.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Wrong credentials!")
    return {"message": "user successfully signed!"}
