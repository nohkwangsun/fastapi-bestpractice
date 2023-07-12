import logging
from functools import wraps

import uvicorn
from fastapi import FastAPI

from decorators import Secured

app = FastAPI()


@app.get("/")
@Secured("admin")
async def root(role: str):
    return {"message": "Hello World, " + role}


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True, log_level=logging.DEBUG)
