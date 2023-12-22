from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Config
from app.routes.v1.family import router as family_router
from app.routes.v1.person import router as person_router
from app.routes.v1.tree import router as tree_router


app = FastAPI(
    title="Silsilah API",
    description="REST API for Silsilah App"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(person_router)
app.include_router(family_router)
app.include_router(tree_router)


@app.get("/")
async def root() -> dict:
    return { "msg": "OK!" }