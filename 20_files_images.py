from fastapi import FastAPI , File , HTTPException , UploadFile 
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#step-1 Ensure folder exists
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

#step-2 static file setup   # this provide actual file via url like http://127.0.0.1:8000/files/filename.png
app.mount("/files", StaticFiles(directory=UPLOAD_FOLDER), name="files")


#step-3 Upload file API
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not filename:
        raise HTTPException(status_code=400, detail="No file uploaded.")
    
    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message":"file uploaded successfully" , 
            "filename":filename ,
            "file_url":f"http://127.0.0.1:8000/files/{filename}"}


#step - 4 get file API
@app.get("/files/{filename}")   
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    
    return {
        "file_url":f"http://127.0.0.1:8000/files/{filename}"}


@app.get("/")
def home():
    return {"message":"Welcome to file upload API"}




