from flask import Flask, render_template, request
import models.db as db
from models import detalle_partido, equipo, partido
from models.equipo import Equipo
from models.partido import Partido

db.Base.metadata.create_all(db.engine)

app = Flask(__name__)


@app.route('/')
def index():
    return "hola mundo"


@app.route('/equipos/', methods=["GET", "POST"])
def equipos():
    if request.method == 'POST':
        equipo_1 = request.form.get("equipo_1")
        equipo_2 = request.form.get("equipo_2")
        equipo_3 = request.form.get("equipo_3")
        equipo_4 = request.form.get("equipo_4")

        equipo = Equipo(equipo_1)
        db.session.add(equipo)
        equipo = Equipo(equipo_2)
        db.session.add(equipo)
        equipo = Equipo(equipo_3)
        db.session.add(equipo)
        equipo = Equipo(equipo_4)
        db.session.add(equipo)
        db.session.commit()
    equipos = db.session.query(Equipo).all()
    return render_template("equipos.html", equipos=equipos)


@app.route('/partidos/', methods=["GET", "POST"])
def partidos():
    if request.method == 'POST':
        partido_1 = request.form.get("partido_1")
        partido_2 = request.form.get("partido_2")
        partido_3 = request.form.get("partido_3")
        partido_4 = request.form.get("partido_4")

        partido = Partido(partido_1)
        db.session.add(partido)
        partido = Partido(partido_2)
        db.session.add(partido)
        partido = Partido(partido_3)
        db.session.add(partido)
        partido = Partido(partido_4)
        db.session.add(partido)
        db.session.commit()

    partidos = db.session.query(Partido).all()
    equipo_1 = db.session.query(Producto).count()
    return render_template("partidos.html", partidos=partidos)


if __name__ == '__main__':
    app.run()
