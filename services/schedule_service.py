from dao.schedule_dao import ScheduleDAO

class ScheduleService:
    """
    Класс Service является вторым слоем, который работает с бизнес-логикой

    Методы данного класса обрабатывают данные,
    После чего они отдаются в следующий слой DAO.
    """
    def __init__(self, dao: ScheduleDAO):
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

    def get_one(self, sid: int):
        """
        Возвращает экземпляр модели.
        """
        return self.dao.get_one(sid)

    def create(self, data):
        """
        Создаёт экземпляр модели и возвращает его.
        """
        return self.dao.create(data)

    def update(self, data, sid: int):
        """
        Обновляет все данные экземпляра модели.
        """
        lecture = self.dao.get_one(sid)

        lecture.title = data.get("title")
        lecture.date = data.get("date")
        lecture.teacher_name = data.get("teacher_name")
        lecture.cabinet_num = data.get("cabinet_num")

        self.dao.update(lecture)

    def update_partial(self, data, sid: int):
        """
        Обновляет переданные данные экземпляра модели.
        """
        lecture = self.dao.get_one(sid)

        if "title" in data:
            lecture.text = data.get("title")
        if "date" in data:
            lecture.text = data.get("date")
        if "teacher_name" in data:
            lecture.text = data.get("teacher_name")
        if "cabinet_num" in data:
            lecture.text = data.get("cabinet_num")

        self.dao.update(lecture)

    def delete(self, sid: int):
        """
        Удаляет экземпляр модели
        """
        self.dao.delete(sid)
