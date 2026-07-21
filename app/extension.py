from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def createControllers(app):
    from app.controllers.clienteController import clienteController, clientBP
    from app.controllers.enderecoController import EnderecoController, enderecoBP

    app.register_blueprint(clientBP)
    app.register_blueprint(enderecoBP)