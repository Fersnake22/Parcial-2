
from bbdd import obtener_db


def insertar_dato(name, code, tiempo, tcode, porcentaje):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "INSERT INTO datos(name, code, tiempo, tcode, porcentaje) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sentencia, [name, code, tiempo, tcode, porcentaje])
    db.commit()
    return True

def obtener_datos():
    db = obtener_db()
    cursor = db.cursor()
    query = "SELECT id, name, code, tiempo, tcode, porcentaje FROM datos"
    cursor.execute(query)
    return cursor.fetchall()

def eliminar_dato(id):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "DELETE FROM datos WHERE id = ?"
    cursor.execute(sentencia, [id])
    db.commit()
    return True

def obtener_dato_por_id(id):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "SELECT id, name, code, tiempo, tcode, porcentaje FROM datos WHERE id = ?"
    cursor.execute(sentencia, [id])
    return cursor.fetchone()

def actualizar_dato(id, name, code, tiempo, tcode, porcentaje):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "UPDATE datos SET name = ?, code = ?, tiempo = ?, tcode = ?, porcentaje= ? WHERE id = ?"
    cursor.execute(sentencia, [name, code, tiempo, tcode, porcentaje, id])
    db.commit()
    return True
