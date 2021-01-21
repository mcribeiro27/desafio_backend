import datetime
from email.policy import default
from time import timezone
from certificado.ext.database import db


class Certificado(db.Model):
    __tablename__ = 'certificado'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    expiration = db.Column(db.Integer)
    expirated_at = db.Column(db.String(15))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    groups = db.relationship('Group')


    def __init__(self, id, username, name, description, expiration, expirated_at):
        self.id = id
        self.username = username
        self.name = name
        self.description = description
        self.expiration = expiration
        self.expirated_at = expirated_at


    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'description': self.description,
            'expiration': self.expiration,
            'expirated_at': self.expirated_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'groups': [group.json() for group in self.groups]
        }

    @classmethod
    def find_certificado(cls, id):
        certificado = cls.query.filter_by(id=id).first()
        if certificado:
            return certificado
        return None

    
    @classmethod
    def find_username(cls, username):
        certificado = cls.query.filter_by(username=username).first()
        if certificado:
            return certificado
        return None


    def save_certificado(self):
        db.session.add(self)
        db.session.commit()

    def update_certificado(self, username, name, description, expiration, expirated_at):
        self.username = username
        self.name = name
        self.description = description
        self.expiration = expiration
        self.expirated_at = expirated_at


    def delete_certificado(self):
        db.session.delete(self)
        db.session.commit()
    