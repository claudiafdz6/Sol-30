from . import db
from flask_login import UserMixin
from datetime import datetime

class TicketSupervisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utente_apertura = db.Column(db.String(64), nullable=False)
    utente_segnalato = db.Column(db.String(64), nullable=False)
    id_task = db.Column(db.String(64), nullable=False)
    note = db.Column(db.Text, nullable=True)
    tag = db.Column(db.String(64), nullable=True)
    data_apertura = db.Column(db.DateTime, default=datetime)
    data_chiusura = db.Column(db.DateTime, nullable=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)