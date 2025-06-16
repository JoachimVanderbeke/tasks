# Want to test it out? Run
# poetry run uvicorn main:app --reload
# Then, navigate to http://127.0.0.1:8000/api/health-check/ in your browser. You should see {"message": "OK"}.

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


@app.get("/api/health-check/")
def health_check():
    return {"message": "OK"}


handle = Mangum(app)  # new
