from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# from authorization.token import fake_decode_token
from authorization import model
from authorization import constants as cc


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return get_user(cc.fake_users_db, token)


def fake_hash_password(password: str):
    return f"fakehashed{password}"


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return model.UserInDB(**user_dict)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    if user := fake_decode_token(token):
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_active_user(current_user: model.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
