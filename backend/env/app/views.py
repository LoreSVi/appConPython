from flask import jsonify, request
from app.models import Reserva

import logging

def index():
    return jsonify({'message': 'Bienvenido API LGM Hotels'})

def create_reserva():    
    data = request.json    
    new_reserva = Reserva(titular=data['titular'], tipo_reserva=data['tipo_reserva'], lugar=data['lugar'], fecha_desde=data['fecha_desde'], fecha_hasta=data['fecha_hasta'])
    new_reserva.save()
    return jsonify({'message': 'Reserva creada con exito'}), 201

def get_all_reservaciones():
    reservaciones = Reserva.get_all()
    return jsonify([reserva.serialize() for reserva in reservaciones])

def get_reserva(id_reserva):
    reserva = Reserva.get_by_id(id_reserva)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    return jsonify(reserva.serialize())

def update_reserva(id_reserva):
    reserva = Reserva.get_by_id(id_reserva)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    data = request.json
    reserva.titular = data['titular']
    reserva.tipo_reserva = data['tipo_reserva']
    reserva.lugar = data['lugar']
    reserva.fecha_desde = data['fecha_desde']
    reserva.fecha_hasta = data['fecha_hasta']
    reserva.save()
    return jsonify({'message': 'Reserva actualizada exitosamente'})

def delete_reserva(id_reserva):
    reserva = Reserva.get_by_id(id_reserva)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    reserva.delete()
    return jsonify({'message': 'Reserva eliminada satisfactoriamente'})