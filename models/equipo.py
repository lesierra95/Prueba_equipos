from sqlalchemy import Column, Integer, String, Float

from models import db


class Equipo(db.Base):
    __tablename__ = 'equipo'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f'Equipo({self.nombre})'

    def __str__(self):
        return self.nombre