from fastapi import FastAPI

app = FastAPI()


#home route
@app.get("/")
def home():
    return {"message": "this is fastapi !!!"}

#about route
@app.get("/about")
def about():
    return {"message": "this is about page !!!"}

#user route
@app.get("/users")
def user():
    return {
        "users":["karan", "sahil", "rohit", "rahul"]
    }