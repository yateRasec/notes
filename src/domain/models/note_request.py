from pydantic import BaseModel


class NoteRequest(BaseModel):
    title: str
    description: str


class TextRequest(BaseModel):
    text: str
