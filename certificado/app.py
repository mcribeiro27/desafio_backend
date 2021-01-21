from flask import Flask
from certificado.ext import configuration, database, commands

from certificado.views.certificado import certificado
from certificado.views.group import grupo


app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
commands.init_app(app)

app.register_blueprint(certificado)
app.register_blueprint(grupo)
