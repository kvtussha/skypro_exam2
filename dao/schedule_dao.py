from dao.models.schedule import Schedule


class ScheduleDAO:
    """
    Класс DAO является третьим слоем, который работает с базой данных.

    Методы данного класса обращаются к базе данных
    И отдают различные данные из нее.
    """

    def __init__(self, session):
        """
        Передается база данных
        """
        self.session = session

    def get_all(self):
        """
        Возвращает список с экземплярами модели.
        """
        return self.session.query(Schedule).all()

    def get_one(self, sid: int):
        """
        Возвращает экземпляр модели.
        """
        return self.session.query(Schedule).get(sid)

    def create(self, data):
        """
        Создает экземпляр модели
        И кладет его в базу данных.

        Возвращает экземпляр модели.
        """
        schedule = Schedule(**data)

        self.session.add(schedule)
        self.session.commit()

        return schedule

    def update(self, schedule: Schedule):
        """
        Кладет обновленный экземпляр модели в базу данных.
        """
        self.session.add(schedule)
        self.session.commit()

    def delete(self, sid: int):
        """
        Удаляет экземпляр модели из базы данных.
        """
        schedule = self.get_one(sid)

        self.session.delete(schedule)
        self.session.commit()
