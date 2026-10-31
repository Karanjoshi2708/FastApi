from fastapi import FastAPI , status , HTTPException

app = FastAPI()

@app.post("/create_user" , status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "msg":"user created"
    }

@app.get("/user")
def get_users():
    return {
        "status":"success",
        "message":"user fetched" ,
        "data":{
            "name":"karan",
            "age":20
            }
    }

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id" : 1 ,
        "name":"karan"
    }
       