from fastapi import FastAPI
from app.routers.link import router as linkrouter

app = FastAPI()

app.include_router(linkrouter)
