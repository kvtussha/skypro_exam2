from setup_db import db
from marshmallow import Schema, fields


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date = db.Column(db.String(20))
    teacher_name = db.Column(db.String(50))
    cabinet_num = db.Column(db.Integer)


class ScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    date = fields.Str()
    teacher_name = fields.Str()
    cabinet_num = fields.Int()
