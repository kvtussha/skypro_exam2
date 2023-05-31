from dao.models.note import Note


class NoteDAO:
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
        return self.session.query(Note).all()

    def get_one(self, nid: int):
        """
        Возвращает экземпляр модели.
        """
        return self.session.query(Note).get(nid)

    def create(self, data):
        """
        Создает экземпляр модели
        И кладет его в базу данных.

        Возвращает экземпляр модели.
        """
        note = Note(**data)

        self.session.add(note)
        self.session.commit()

        return note

    def update(self, note: Note):
        """
        Кладет обновленный экземпляр модели в базу данных.
        """
        self.session.add(note)
        self.session.commit()

    def delete(self, nid: int):
        """
        Удаляет экземпляр модели из базы данных.
        """
        note = self.get_one(nid)

        self.session.delete(note)
        self.session.commit()
