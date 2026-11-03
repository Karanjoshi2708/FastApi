from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Allowed origin (frontend url)
origins = [
    "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   #allowed frontend url
    allow_credentials=True,
    allow_methods=["*"], #get, post, put, delete
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message":"hello cors !!!"}