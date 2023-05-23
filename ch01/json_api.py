from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/test", response_class=JSONResponse)
def test_endpoint():
    return {"response": "this is a response", "key_2": 'key '}


@app.get("/", response_class=JSONResponse)
def home():
    return {"response": "this is a home"}


