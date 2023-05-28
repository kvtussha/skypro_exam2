from flask import request
from flask_restx import Resource, Namespace

from model.note import Note, NoteSchema
from setup_db import db

note_ns = Namespace("notes")
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


@note_ns.route("/")
class NotesView(Resource):
    def get(self):
        """Getting all the notes"""
        notes = db.session.query(Note).all()
        return notes_schema.dump(notes), 200

    def post(self):
        """Adding one note"""
        req_json = request.json
        note = Note(**req_json)
        db.session.add(note)
        db.session.commit()

        return "", 204


@note_ns.route("/<int:nid>")
class NoteView(Resource):
    def get(self, nid: int):
        note = db.session.query(Note).get(nid)
        return note_schema.dump(note), 200

    def put(self, nid: int):
        """Updating a note"""
        note = db.session.query(Note).get(nid)
        data = request.json

        if "text" in data:
            note.text = data.get('text')

        db.session.add(note)
        db.session.commit()

        return "", 204

    def delete(self, nid: int):
        """Deleting a Note"""
        note = db.session.query(Note).get(nid)
        db.session.delete(note)
        db.session.commit()

        return "", 204
