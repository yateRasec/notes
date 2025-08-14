from __future__ import annotations
from typing import Optional, List
from dataclasses import dataclass

from src.domain.models.note_request import NoteRequest


@dataclass
class Note:
    title: str
    description: str
    id: Optional[str] = None

    @staticmethod
    def map_from_request(data: NoteRequest, id: Optional[int] = None) -> Note:
        if id:
            return Note(
                title=data.title.strip(),
                description=data.description.strip(),
                id=id,
            )
        return Note(title=data.title.strip(), description=data.description.strip())

    @staticmethod
    def map_from_db(data) -> Note:
        return Note(
            title=data.get("title"),
            description=data.get("description"),
            id=data.get("id"),
        )

    @staticmethod
    def map_list_from_db(data) -> List[Note]:
        return [Note.map_from_db(item) for item in data]
