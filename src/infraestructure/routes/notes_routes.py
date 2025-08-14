from fastapi import APIRouter, status, Depends

from src.infraestructure.database.sqlite.dependency import get_db
from src.domain.models.note_request import NoteRequest
from src.core.models.response import Response
from src.domain.use_cases.note_use_case import NoteUseCase
from src.infraestructure.database.sqlite.connection import HandlerSQLite
from src.infraestructure.database.sqlite.repositories.note_repository import (
    NoteRepository,
)

# from src.domain.models.note_request import NoteRequest


note_routes = APIRouter(
    prefix="/note",
    tags=["Note"],
    responses={404: {"description": "Not found"}},
)

note_use_case = NoteUseCase(NoteRepository())


@note_routes.get("/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def get_one_note(id: int, db=Depends(get_db)) -> Response:
    return note_use_case.execute_get_notes(db, id)


@note_routes.get("/", status_code=status.HTTP_200_OK, response_model=Response)
def get_all_note(db=Depends(get_db)) -> Response:
    return note_use_case.execute_get_notes(db)


@note_routes.post("/", status_code=status.HTTP_200_OK, response_model=Response)
def save_note(note: NoteRequest, db=Depends(get_db)) -> Response:
    return note_use_case.execute_save_note(note, db)


@note_routes.put("/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def update_note(id: int, note: NoteRequest, db=Depends(get_db)) -> Response:
    return note_use_case.execute_update_note(id, note, db)


@note_routes.delete("/{id}", status_code=status.HTTP_200_OK, response_model=Response)
def delete_note(id: int, db=Depends(get_db)) -> Response:
    return note_use_case.execute_delete_note(id, db)


@note_routes.post("/create_table", status_code=status.HTTP_200_OK, response_model=Response)
def create_table(db=Depends(get_db)) -> Response:
    return note_use_case.execute_create_table(db)
