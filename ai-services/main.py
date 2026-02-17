from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Grievance Backend Running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "OK"}
