import os
from fastapi import FastAPI, APIRouter

base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])

@base_router.get("/")
def welcome():
    app_name = os.getenv("App_Name")
    app_version = os.getenv("App_Version")
    return {
        "app_name": app_name,
        "app_version": app_version
    }

