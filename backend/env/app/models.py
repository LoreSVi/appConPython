from app.database import get_db

import logging

class Reserva:
    
    def __init__(self, id_reserva=None, titular=None, tipo_reserva=None, lugar=None, fecha_desde=None, fecha_hasta=None):
        self.id_reserva = id_reserva
        self.titular = titular
        self.tipo_reserva = tipo_reserva
        self.lugar = lugar
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_reserva:
            cursor.execute("""
                UPDATE reservaciones SET titular = %s, tipo_reserva = %s, lugar = %s, fecha_desde = %s, fecha_hasta = %s  WHERE id_reserva = %s
                """, (self.titular, self.tipo_reserva, self.lugar, self.fecha_desde, self.fecha_hasta, self.id_reserva))
        else:
            cursor.execute("""INSERT INTO reservaciones (titular, tipo_reserva, lugar, fecha_desde, fecha_hasta) VALUES (%s, %s, %s, %s, %s)""", (self.titular, self.tipo_reserva, self.lugar, self.fecha_desde, self.fecha_hasta))
            self.id_reserva = cursor.lastrowid
        db.commit()
        cursor.close()
       
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservaciones")
        rows = cursor.fetchall()
        reservaciones = [Reserva(id_reserva=row[0], titular=row[1], tipo_reserva=row[2], lugar=row[3], fecha_desde=row[4], fecha_hasta=row[5]) for row in rows]
        cursor.close()
        return reservaciones

    @staticmethod
    def get_by_id(id_reserva):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reservaciones WHERE id_reserva = %s", (id_reserva,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(id_reserva=row[0], titular=row[1], tipo_reserva=row[2], lugar=row[3], fecha_desde=row[4], fecha_hasta=row[5])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reservaciones WHERE id_reserva = %s", (self.id_reserva,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_reserva': self.id_reserva,
            'titular': self.titular,
            'tipo_reserva': self.tipo_reserva,
            'lugar': self.lugar,
            'fecha_desde': self.fecha_desde.strftime('%Y-%m-%d'),
            'fecha_hasta': self.fecha_hasta.strftime('%Y-%m-%d'),
        }


