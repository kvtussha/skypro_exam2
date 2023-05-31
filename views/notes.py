from flask import request
from flask_restx import Resource, Namespace

from implemented import note_service, note_schema, notes_schema

note_ns = Namespace("notes")


@note_ns.route("/")
class NotesView(Resource):
    """
    Класс View является первым слоем, который работает с HTTP запросами
    И его методами GET/POST/PUT/PATCH/DELETE

    Работа класса заключается в том, что он обрабатывает запрос пользователя
    И передаёт данные о запросе в следующий слой Service.
    """
    def get(self):
        """
        ПОЛУЧЕНИЕ ВСЕХ ЗАМЕТОК

        В notes хранится список с экземплярами нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        notes = note_service.get_all()
        return notes_schema.dump(notes), 200

    def post(self):
        """
        СОЗДАНИЕ НОВЫХ ЗАМЕТОК

        Сначала получаем данные от пользователя в req_json.
        Затем создаем экземпляр модели в переменной note
        И сохраняем его в базу данных.

        Возвращаем экземпляр в формате json с помощью схемы.
        """
        req_json = request.json
        note = note_service.create(req_json)

        return note_schema.dump(note), 201


@note_ns.route("/<int:nid>")
class NoteView(Resource):
    def get(self, nid: int):
        """
        ПОЛУЧЕНИЕ ЗАМЕТКИ ПО ЕЁ ID

        В note хранится экземпляр нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        note = note_service.get_one(nid)
        return note_schema.dump(note), 200

    def put(self, nid: int):
        """
        ПОЛНОЕ ОБНОВЛЕНИЕ ЗАМЕТКИ ПО ЕЁ ID

        Сначала получаем данные от пользователя в req_json.
        Обновляем экземпляр модели по ее id.

        В note хранится экземпляр нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        req_json = request.json
        note_service.update(req_json, nid)

        note = note_service.get_one(nid)
        return note_schema.dump(note), 202

    def patch(self, nid: int):
        """
        ЧАСТИЧНОЕ ОБНОВЛЕНИЕ ЗАМЕТКИ ПО ЕЁ ID

        Сначала получаем данные от пользователя в req_json.
        Обновляем экземпляр модели по ее id.

        В note хранится экземпляр нашей модели из базы данных.
        Возвращаем его в формате json с помощью схемы.
        """
        req_json = request.json
        note_service.update_partial(req_json, nid)

        note = note_service.get_one(nid)
        return note_schema.dump(note), 202

    def delete(self, nid: int):
        """
        УДАЛЕНИЕ ЗАМЕТКИ ПО ЕЁ ID

        Удаляем экземпляр модели по ее id из базы данных.
        Возвращаем сообщение о том, что заметка удалена.
        """
        note_service.delete(nid)
        response = {"message": "Заметка удалена"}

        return response, 200
