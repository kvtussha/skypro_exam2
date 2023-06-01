from dao.schedule_dao import ScheduleDAO
from services.schedule_service import ScheduleService
from dao.models.schedule import ScheduleSchema

from setup_db import db


schedule_dao = ScheduleDAO(db.session)
schedule_service = ScheduleService(schedule_dao)

lecture_schema = ScheduleSchema()
lectures_schema = ScheduleSchema(many=True)
