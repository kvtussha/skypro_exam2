from dao.note_dao import NoteDAO

class NoteService:
    """
    Класс Service является вторым слоем, который работает с бизнес-логикой

    Методы данного класса обрабатывают данные,
    После чего они отдаются в следующий слой DAO.
    """
    def __init__(self, dao: NoteDAO):
        """
        В сервис передается нужный DAO
        Для дальнейшей работы с базой данных
        """
        self.dao = dao

    def get_all(self):
        """
        Возвращает список с экземплярами модели.
        """
        return self.dao.get_all()

    def get_one(self, nid: int):
        """
        Возвращает экземпляр модели.
        """
        return self.dao.get_one(nid)

    def create(self, data):
        """
        Создаёт экземпляр модели и возвращает его.
        """
        return self.dao.create(data)

    def update(self, data, nid: int):
        """
        Обновляет все данные экземпляра модели.
        """
        note = self.dao.get_one(nid)

        note.text = data.get("text")

        self.dao.update(note)

    def update_partial(self, data, nid: int):
        """
        Обновляет переданные данные экземпляра модели.
        """
        note = self.dao.get_one(nid)

        if "text" in data:
            note.text = data.get("text")

        self.dao.update(note)

    def delete(self, nid: int):
        """
        Удаляет экземпляр модели
        """
        self.dao.delete(nid)
