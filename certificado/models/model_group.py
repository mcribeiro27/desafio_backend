from certificado.ext.database import db


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    certificado_id = db.Column(db.Integer, db.ForeignKey('certificado.id'))

    def __init__(self, id, name, certificado_id):
        self.id = id
        self.name = name
        self.certificado_id = certificado_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @classmethod
    def find_group(cls, id):
        group = cls.query.filter_by(id=id).first()
        if group:
            return group
        return group

    def save_group(self):
        db.session.add(self)
        db.session.commit()

    def update_group(self, name, certificado_id):
        self.name = name
        self.certificado_id = certificado_id
    
    def delete_group(self):
        db.session.delete(self)
        db.session.commit()