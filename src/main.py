from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from src.infraestructure.routes.notes_routes import note_routes

app = FastAPI()

origins = [
    "http://localhost:4000",
]

# Agregar middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(note_routes)
