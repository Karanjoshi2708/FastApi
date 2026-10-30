from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    

app = FastAPI()

@app.post("/create-user")
def create_user(user:User):
    return {
        "msg":"data created",
        "data":user
    }

