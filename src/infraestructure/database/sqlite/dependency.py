from src.infraestructure.database.sqlite.connection import HandlerSQLite


def get_db():
    db = HandlerSQLite()
    try:
        yield db
    finally:
        db.close()
