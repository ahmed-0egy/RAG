from fastapi import FastAPI

app = FastAPI()


"""
   The following block of code creates a function called "simple_api_fun".
   To make this function act as an API we add a decorator(a fastapi decorator) before it.
   The name of the api we created is called "Welcome".
"""

@app.get("/welcome")
def simple_api_fun():
    return {
        "message": "Welcome to FastAPI!"
    }
