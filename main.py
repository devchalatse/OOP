from fastapi import FastAPI, Form
from typing import Annotated
from model import User

app = FastAPI()

@app.post('/login')
async def login(new:Annotated[User, Form()]):
    return new





