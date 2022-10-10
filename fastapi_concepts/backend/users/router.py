from fastapi import APIRouter
from users import controllers

user_api_router = APIRouter()

user_api_router.include_router(controllers.router, prefix="/user", tags=["User"])
