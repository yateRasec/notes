from typing import Optional, List, Union
from src.domain.models.note_request import NoteRequest
from src.core.models.response import Response
from src.domain.models.note import Note
from src.domain.repositories.note_repository import INoteRepository


class NoteUseCase:
    def __init__(self, note_repository: INoteRepository) -> None:
        self.note_repository = note_repository

    def execute_get_notes(self, db, id: Optional[int] = "") -> Union[Note, List[Note]]:
        if id:
            data = self.note_repository.get_note(id, db)
            if data:
                return Response.success(response=data)
            return Response.success(message="No se encontro data")

        data = self.note_repository.get_all_notes(db)
        if data:
            return Response.success(response=data)
        return Response.success(message="No se encontro data")

    def execute_save_note(self, note: NoteRequest, db) -> Note:
        note_domain = Note.map_from_request(note)
        data = self.note_repository.save_note(note_domain, db)
        if data:
            return Response.success(response=data)
        return Response.success(message="No se logro guardar la información")

    def execute_update_note(self, id: int, note: NoteRequest, db) -> Note:
        note_domain = Note.map_from_request(note, id)
        data = self.note_repository.update_note(note_domain, db)
        if data:
            return Response.success(response=data)
        return Response.success(
            message="No se logro actualizar la información, el registro no existe"
        )

    def execute_delete_note(self, id: int, db) -> Note:
        data = self.note_repository.delete_note(id, db)
        if data:
            return Response.success(response=data)
        return Response.success(
            message="No se logro eliminar la información, el registro no existe"
        )

    def execute_create_table(self, db) -> None:
        self.note_repository.create_note_table(db)
        return Response.success(response="creada la tabla")
