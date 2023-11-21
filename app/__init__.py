from fastapi import FastAPI


app = FastAPI(
    title="Silsilah API",
    description="REST API for Silsilah App"
)

@app.get("/")
async def root() -> dict:
    return { "msg": "OK!" }