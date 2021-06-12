from sqlalchemy import Column, Integer, String, Float

from models import db


class Partido(db.Base):
    __tablename__ = 'partido'

    id = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False)

    def __init__(self, numero):
        self.numero = numero

    def __repr__(self):
        return f'Partido({self.numero})'

    def __str__(self):
        return self.numero