from . import db
from flask_sqlalchemy import SQLAlchemy
from datetime import date

class NetSign(db.Model):
    __tablename__ = 'jnfdc_net_sign'
    id = db.Column(db.Integer, primary_key=True)
    signnum = db.Column(db.Integer)
    date = db.Column(db.Date, default=date.today(), unique=True)

    def add(self):
        db.session.add(self)
        db.session.commit()
