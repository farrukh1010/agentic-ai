from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def chat(query: str):
    return {
        "name": "farrukh zaman"
    }