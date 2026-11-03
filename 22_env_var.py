from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()  # Load environment variables from .env file

#Allowed origin (frontend url)
ORIGINS = os.getenv("ORIGINS")  # Get the allowed origins from environment variable

SECRET_KEY = os.getenv("SECRET_KEY")  
DB_URL = os.getenv("DB_URL")  # Get the database URL from environment variable

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