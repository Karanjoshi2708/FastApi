from fastapi import FastAPI , Depends , HTTPException
from jose import jwt
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from datetime import datetime , timedelta, timezone
from passlib.context import CryptContext

app = FastAPI() 

#JWt COnfiguration
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


#password hashing  
pwd_context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

#OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


#DUmmy user database
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("1234")
    }
}

#hash password
def hash_password(password:str):
    return pwd_context.hash(password)

#verify password
def verify_password(plain_password:str , hashed_password:str):
    return pwd_context.verify(plain_password , hashed_password)

#create token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update(
        {"exp":expire})
    
    token = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)

    return token

#Login API(OAuth2 form)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password , user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="invalid username or password"
        )
    else:
        access_token = create_token({
            "sub":form_data.username
            })
        return {
            "access_token":access_token,
            "token_type":"bearer"
        }
    
#Token verify
def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="invalid token or expired token"
            )
        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="invalid token or expired token"
        )


#protected route
@app.get("/secure")
def secure_data(user:str = Depends(verify_token)):
    return {
        "msg":"this is secure route",
        "user":user
    }