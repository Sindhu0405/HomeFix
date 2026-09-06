from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import appliances, diagnosis, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HomeFix API",
    description="AI-ready appliance troubleshooting and maintenance platform",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(appliances.router)
app.include_router(diagnosis.router)
app.include_router(auth.router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "homefix-api"
    }