from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def createControllers(app):
    from app.controllers.clienteController import clienteController, clientBP
    from app.controllers.enderecoController import EnderecoController, enderecoBP
    from app.controllers.onibusController import OnibusController, onibusBP
    from app.controllers.excursaoController import ExcursaoController, excursaoBP
    from app.controllers.vendaController import reservaController, reservaBP

    app.register_blueprint(clientBP)
    app.register_blueprint(enderecoBP)
    app.register_blueprint(onibusBP)
    app.register_blueprint(excursaoBP)
    app.register_blueprint(reservaBP)