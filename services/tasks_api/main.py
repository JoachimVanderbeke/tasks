from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum  # new

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# poetry run uvicorn main:app --reload
# navigate to http://127.0.0.1:8000/api/health-check/
@app.get("/api/health-check/")
def health_check():
    return {"message": "OK"}


handle = Mangum(app)  # new
