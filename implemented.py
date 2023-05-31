from dao.note_dao import NoteDAO
from services.note_service import NoteService
from dao.models.note import NoteSchema

from setup_db import db


note_dao = NoteDAO(db.session)
note_service = NoteService(note_dao)

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
