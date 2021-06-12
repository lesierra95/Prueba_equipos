from sqlalchemy import Column, Integer, String, Float, ForeignKey

from models import db


class Detalle_Partido(db.Base):
    __tablename__ = 'detalle_partido'

    id = Column(Integer, primary_key=True)
    equipo_local = Column(Integer, ForeignKey('equipo.id'))
    equipo_visitante = Column(Integer, ForeignKey('equipo.id'))
    marcador_local = Column(Integer, nullable=False)
    marcador_visitante = Column(Integer, nullable=False)
    partido = Column(Integer, ForeignKey('equipo.id'))

    def __init__(self, equipo_local, equipo_visitante, marcador_local, marcador_visitante, partido):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.marcador_local = marcador_local
        self.marcador_visitante = marcador_visitante
        self.partido = partido

    def __repr__(self):
        ganador = "Local" if self.marcador_local > self.marcador_visitante else "Visitante"
        return f'Ganador({ganador})'
