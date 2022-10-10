from fastapi import APIRouter
from jobs import controllers

job_api_router = APIRouter()

job_api_router.include_router(controllers.router, prefix="/job", tags=["Job"])
