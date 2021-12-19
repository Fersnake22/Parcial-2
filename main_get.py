
from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_datos
import sqlite3 as sql
from bbdd import create_tables, obtener_db

app = Flask(__name__)


@app.route("/tabla")
def datos():
    datos = controlador_datos.obtener_datos()
    return jsonify(datos)


@app.route("/dato", methods=["GET"])
def guardar_dato():
    data_details = request.get_json()
    name = data_details["name"]
    code = data_details["code"]
    tiempo = data_details["tiempo"]
    tcode = data_details["tcode"]
    porcentaje = data_details["porcentaje"]

    resultado = controlador_datos.insertar_dato(name, code, tiempo, tcode, porcentaje)
    return redirect("/datos")
    return jsonify(resultado)




@app.route("/dato", methods=["DELETE"])
def eliminar_dato():
    resultado = controlador_datos.eliminar_dato(data_details["id"])
    return jsonify(resultado)


@app.route("/dato/<int:id>")
def editar_dato(id):
    # Obtener el dato por ID
    dato = controlador_datos.obtener_dato_por_id(id)
    return jsonify(dato)


@app.route("/dato", methods=["PUT"])
def actualizar_dato():
    data_details = request.get_json()
    id = data_details["id"]
    name = data_details["name"]
    code = data_details["code"]
    tiempo = data_details["tiempo"]
    tcode = data_details["tcode"]
    porcentaje = data_details["porcentaje"]
    resultado = controlador_datos.actualizar_dato(name, code, tiempo, tcode, porcentaje, id)
    return jsonify(resultado)

@app.route('/')
def tabla():

    con = sql.connect("sarampion.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from datos")
   
    rows = cur.fetchall();
    return render_template("tabla.html",rows = rows)


# Iniciar el servidor
if __name__ == "__main__":
    create_tables()
 
    app.run(port=8046, debug=False)