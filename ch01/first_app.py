from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "new hello world"

