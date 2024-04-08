from sqlalchemy import Integer, String, Column

from database import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message = Column(String)

    # добавила этот метод для сериализации тоесть для перевода в json формат
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}