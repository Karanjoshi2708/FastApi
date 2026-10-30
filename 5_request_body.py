from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user")
def create_user(name:str, age:int):
    return {
        "name":name,
        "age":age
    }

