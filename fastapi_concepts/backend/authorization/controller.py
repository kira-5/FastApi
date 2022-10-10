from authorization import model
from fastapi import FastAPI, Depends, APIRouter
from authorization.service import get_current_user, fake_hash_password
from fastapi.security import OAuth2PasswordRequestForm
from authorization import constants as cc
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

router = APIRouter()


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = cc.fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    user = model.UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/current-user")
async def current_user(current_user: model.User = Depends(get_current_user)):
    return current_user
