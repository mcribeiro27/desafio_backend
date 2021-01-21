from certificado.ext.database import db

def create_db():
    """ Cria o banco de dados"""
    db.create_all()

def init_app(app):
    for command in [create_db]:
        app.cli.add_command(app.cli.command()(command))