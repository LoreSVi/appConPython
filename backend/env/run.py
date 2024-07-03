from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

import logging

app = Flask(__name__)

# Configurar la aplicación Flask
# app.config.from_pyfile('config/development.py')

# Inicializar la base de datos con la aplicación Flask
init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)
#permitir solicitudes desde un origen específico
#CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})

# Rutas para el CRUD de la entidad Movie
app.route('/', methods=['GET'])(index)
app.route('/api/reservaciones/', methods=['POST'])(create_reserva)
app.route('/api/reservaciones/', methods=['GET'])(get_all_reservaciones)
app.route('/api/reservaciones/<int:id_reserva>', methods=['GET'])(get_reserva)
app.route('/api/reservaciones/<int:id_reserva>', methods=['PUT'])(update_reserva)
app.route('/api/reservaciones/<int:id_reserva>', methods=['DELETE'])(delete_reserva)

if __name__ == '__main__':
#    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(debug=True)
    