from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Las tablas ya existen, no necesitamos crearlas
    yield

app = FastAPI(lifespan=lifespan)
