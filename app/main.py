from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running inside Docker"}

@app.get("/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello {name}"
    }
