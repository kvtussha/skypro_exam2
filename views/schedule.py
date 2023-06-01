from flask import request
from flask_restx import Resource, Namespace

from implemented import schedule_service, lecture_schema, lectures_schema

schedule_ns = Namespace("schedule")


@schedule_ns.route("/")
class SchedulesView(Resource):
    """
    Класс View является первым слоем, который работает с HTTP запросами
    И его методами GET/POST/PUT/PATCH/DELETE

    Работа класса заключается в том, что он обрабатывает запрос пользователя
    И передаёт данные о запросе в следующий слой Service.
    """
    def get(self):
        """
        ПОЛУЧЕНИЕ ВСЕХ ЛЕКЦИЙ

        В lectures хранится список с экземплярами нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        lectures = schedule_service.get_all()
        return lectures_schema.dump(lectures), 200

    def post(self):
        """
        СОЗДАНИЕ НОВЫХ ЛЕКЦИЙ

        Сначала получаем данные от пользователя в req_json.
        Затем создаем экземпляр модели в переменной schedule
        И сохраняем его в базу данных.

        Возвращаем экземпляр в формате json с помощью схемы.
        """
        req_json = request.json
        schedule = schedule_service.create(req_json)

        return lecture_schema.dump(schedule), 201


@schedule_ns.route("/<int:sid>")
class scheduleView(Resource):
    def get(self, sid: int):
        """
        ПОЛУЧЕНИЕ ЛЕКЦИИ ПО ЕЁ ID

        В schedule хранится экземпляр нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        schedule = schedule_service.get_one(sid)
        return lecture_schema.dump(schedule), 200

    def put(self, sid: int):
        """
        ПОЛНОЕ ОБНОВЛЕНИЕ ЛЕКЦИИ ПО ЕЁ ID

        Сначала получаем данные от пользователя в req_json.
        Обновляем экземпляр модели по ее id.

        В schedule хранится экземпляр нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        req_json = request.json
        schedule_service.update(req_json, sid)

        schedule = schedule_service.get_one(sid)
        return lecture_schema.dump(schedule), 202

    def patch(self, sid: int):
        """
        ЧАСТИЧНОЕ ОБНОВЛЕНИЕ ЛЕКЦИИ ПО ЕЁ ID

        Сначала получаем данные от пользователя в req_json.
        Обновляем экземпляр модели по ее id.

        В schedule хранится экземпляр нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        req_json = request.json
        schedule_service.update_partial(req_json, sid)

        schedule = schedule_service.get_one(sid)
        return lecture_schema.dump(schedule), 202

    def delete(self, sid: int):
        """
        УДАЛЕНИЕ ЛЕКЦИИ ПО ЕЁ ID

        Удаляем экземпляр модели по ее id из базы данных.
        Возвращаем сообщение о том, что лекция удалена.
        """
        schedule_service.delete(sid)
        response = {"message": "Лекция удалена"}

        return response, 200
