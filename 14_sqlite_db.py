import sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect('test.db' , check_same_thread=False)
curssor = conn.cursor()

curssor.execute("""
 Create table if not exists todos (
    id INTEGER PRIMARY KEY,
    title TEXT ,
    completed Text 
)
""")

conn.commit()


@app.get("/")
def home():
    return {
        "message":"sqlite connected"
    }


