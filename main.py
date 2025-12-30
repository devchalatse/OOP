from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

@app.post

async def root():
    