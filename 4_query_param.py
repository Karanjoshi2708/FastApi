from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def user(name: str = None):
    return {
        "users":name
    }

@app.get("/products")
def  product(limit:int = 10):
    return {
        "limit":limit
    }


@app.get("/items")
def  product(name:str = None, limit:int = 10):
    return {
        "name":name,
        "limit":limit
    }