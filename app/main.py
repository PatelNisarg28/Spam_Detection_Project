from fastapi import FastAPI
from app.routes import router

# Initialize FastAPI app
app = FastAPI()

# Include prediction routes
app.include_router(router)

@app.get("/")
def welcome():
    """
    Welcome route to test API status.
    
    Returns:
    dict: A message confirming API availability.
    """
    return {"message": "Welcome to the SVM Text Classification API"}
