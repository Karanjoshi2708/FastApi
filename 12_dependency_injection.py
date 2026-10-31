from fastapi import FastAPI , Depends, HTTPException, Header

app = FastAPI()

def verify_token(token:str = Header(None)):
    if token != "karan":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"
        )
    return{
        "user" : "Authorized user"
    }

@app.get("/secure-data")
def get_secure_data(user = Depends(verify_token)):
    return {
        "msg":"this is secure data",
        "user": user
    }

# def commom_logic():
#     return {
#         "msg":"this is common logic"
#     }


# @app.get("/home")
# def home(data = Depends(commom_logic)):
#     return data




# def get_current_user():
#     return {
#         "user":"karan"
#     }

# @app.get("/profile")
# def get_profile(user = Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def get_dashboard(user = Depends(get_current_user)):
#     return user