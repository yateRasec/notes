from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.repositories.iconnection_database import IConnectionDatabase
from src.domain.models.note import Note


class INoteRepository(ABC):
    @abstractmethod
    def get_note(self, id: int, db: IConnectionDatabase) -> Union[Note, None]:
        pass

    @abstractmethod
    def get_all_notes(self, db: IConnectionDatabase) -> Union[List[Note], None]:
        pass

    @abstractmethod
    def save_note(self, note: Note, db: IConnectionDatabase) -> bool:
        pass

    @abstractmethod
    def update_note(self, note: Note, db: IConnectionDatabase) -> bool:
        pass

    @abstractmethod
    def delete_note(self, id: int, db: IConnectionDatabase) -> bool:
        pass

    @abstractmethod
    def create_note_table(self, db: IConnectionDatabase) -> None:
        pass
