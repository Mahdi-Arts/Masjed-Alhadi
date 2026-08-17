from fastapi import FastAPI

app = FastAPI()


@app.get("/api/status")
def status() -> dict:
    return {"status": "OK", "fortress": "MahdiYar"}