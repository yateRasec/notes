from fastapi import FastAPI, Depends

from src.infraestructure.database.sqlite.dependency import get_db
from src.infraestructure.routes.notes_routes import note_routes

app = FastAPI()


app.include_router(note_routes)
