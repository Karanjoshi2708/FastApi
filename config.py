import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
class Settings:
   
    ORIGINS = os.getenv("ORIGINS") 
    SECRET_KEY = os.getenv("SECRET_KEY")  
    DB_URL = os.getenv("DB_URL") 

settings = Settings()