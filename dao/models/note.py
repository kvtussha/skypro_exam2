from setup_db import db
from marshmallow import Schema, fields
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250))
    date = db.Column(db.DateTime, default=func.now())


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str()
    date = fields.DateTime()
