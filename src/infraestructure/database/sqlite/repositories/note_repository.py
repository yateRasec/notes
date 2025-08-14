from typing import List, Union

from src.domain.repositories.iconnection_database import IConnectionDatabase
from src.domain.repositories.note_repository import INoteRepository
from src.domain.models.note import Note


class NoteRepository(INoteRepository):

    def get_note(self, id: int, db: IConnectionDatabase) -> Union[Note, None]:
        cursor = db.run_query(f"SELECT * FROM notes where id='{id}'")
        notes = [dict(row) for row in cursor.fetchall()]

        if notes:
            return Note.map_from_db(notes[0])
        return None

    def get_all_notes(self, db: IConnectionDatabase) -> Union[List[Note], None]:
        cursor = db.run_query("SELECT * FROM notes")
        return Note.map_list_from_db([dict(row) for row in cursor.fetchall()])

    def save_note(self, note: Note, db: IConnectionDatabase) -> bool:
        cursor = db.run_query(
            f"Insert into notes (title, description) values ('{note.title}', '{note.description}')"
        )
        db.confirm()
        cursor.close()
        return True

    def update_note(self, note: Note, db: IConnectionDatabase) -> bool:
        if not note.id:
            return False

        find_note = self.get_note(note.id, db)
        if not find_note:
            return False

        cursor = db.run_query(
            f"UPDATE notes SET title = '{note.title}', description = '{note.description}' WHERE id = '{note.id}'; "
        )
        db.confirm()
        cursor.close()
        return True

    def delete_note(self, id: int, db: IConnectionDatabase) -> bool:

        find_note = self.get_note(id, db)
        if not find_note:
            return False

        cursor = db.run_query(f"Delete from notes where id = '{id}'")
        db.confirm()
        cursor.close()
        return True

    def create_note_table(self, db: IConnectionDatabase) -> bool:

        db.run_query(
            """
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL
                );
            """
        )
        db.confirm()
        db.close()
        return True
