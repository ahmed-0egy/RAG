from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env") # this must be before importing any other python file so that any python file can see the environment variables loaded in main.py using this line of code.
from routes import base

app = FastAPI()

app.include_router(base.base_router)
