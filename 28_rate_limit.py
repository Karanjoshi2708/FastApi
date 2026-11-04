from fastapi import FastAPI , Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse


app = FastAPI()

#Limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

#Error handler for rate limit exceeded
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):  
    return JSONResponse(
        status_code=429,
        content={"message": "Rate limit exceeded. Please try again later."},
    )

#Rate limiter API 
@app.get("/limited")
@limiter.limit("5/minute")  # Limit to 5 requests per minute
def limited_endpoint(request: Request):
    return {"message": "This endpoint is rate limited to 5 requests per minute."}
