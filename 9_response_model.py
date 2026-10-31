from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

#to hide sensitive data
#request - client to server
#response - server to client

@app.get("/user" , response_model=UserResponse)
def get_user():
    return {
        "name":"karan",
        "age":"20a" ,
        "password":"1234"
        }