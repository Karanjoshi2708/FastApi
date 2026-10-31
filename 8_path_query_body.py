from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name:str
    age:int


@app.post("/user")
def create_user(user:User):
    users.append(user)
    return {
        "msg":"user created",
        "data":user
    }

#Ex.http://127.0.0.1:8000/user/0?notify=true

@app.put("/user/{user_id}")
def update_user(user_id:int, user:User , notify:bool = False):
    if user_id < len(users):
        users[user_id] = user
        return {
            "msg":"user updated",
            "notify":notify,
            "data":user
            
        }
    return {
        "error ":"user not found"}