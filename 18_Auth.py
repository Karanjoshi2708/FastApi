from fastapi import FastAPI , Depends , HTTPException , Header
from jose import jwt
from datetime import datetime , timedelta, timezone

app = FastAPI() 

SECRET_KEY = "mysecret"

ALGORITHM = "HS256"

#create token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update(
        {"exp":expire})
    
    token = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)

    return token

#Login API(Generate token)
@app.post("/login")
def login(username:str , password:str):
    if username != "admin" and password != "1234":
        raise HTTPException(
            status_code=401,
            detail="invalid username or password"
        )
    else:
        token = create_token({
            "sub":username
            })
        
        return {
            "access_token":token
        }

#Token verify
def verify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="invalid token or expired token"
        )

#protected route
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return {
        "msg":"this is secure route",
        "user":user
    }