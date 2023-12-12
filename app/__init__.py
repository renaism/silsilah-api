from fastapi import FastAPI

from app.routes.v1.family import router as family_router
from app.routes.v1.person import router as person_router
from app.routes.v1.tree import router as tree_router


app = FastAPI(
    title="Silsilah API",
    description="REST API for Silsilah App"
)


@app.get("/")
async def root() -> dict:
    return { "msg": "OK!" }


# Routers
app.include_router(person_router)
app.include_router(family_router)
app.include_router(tree_router)