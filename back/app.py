from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)

# Conexión local a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["juegos_db"]
collection = db["juegos"]

# Crear indice unico por campo 'id' para persistencia
collection.create_index("id", unique=True)

# Eliminar todos los datos de la BDD -> collection.delete_many({})


# Ruta principal - muestra los juegos - GET
@app.route('/')
def index():
    juegos = list(collection.find())
    return render_template("index.html", juegos=juegos)


# Ruta del formulario para crear juegos
@app.route('/form')
def form():
    return render_template("form.html")


# Ruta que recibe los datos POST de cada Juego - invocada por el submit del form
@app.route('/agregar', methods=["POST"])
def agregar():
    # Buscar el último juego ingresado, ordenado por 'id' descendente
    ultimo = collection.find_one(sort=[("id", -1)])
    nuevo_id = (ultimo["id"] + 1) if ultimo and "id" in ultimo else 1

    juego = {
        "id": nuevo_id,
        "nombre": request.form['nombre'],
        "jugadores_min": request.form['jugadores_min'],
        "jugadores_max": request.form['jugadores_max'],
        "edad": request.form['edad'],
        "pais": request.form['pais'],
        "costo": request.form['costo']
    }

    try:
        collection.insert_one(juego)
    except DuplicateKeyError:
        return "Error: Ya existe un juego con ese ID."

    return redirect('/')


# Ruta para DELETE
@app.route('/eliminar/<int:id>', methods=["POST"])
def eliminar(id):
    collection.delete_one({"id": id})
    return redirect('/')


# Ruta para PATCH
@app.route('/editar/<int:id>')
def editar(id):
    juego = collection.find_one({"id": id})
    if not juego:
        return "Juego no encontrado", 404
    return render_template("editar.html", juego=juego)


# Ruta invocada por el submit de editar - modifica los nuevos cambios en un juego
@app.route('/actualizar/<int:id>', methods=["POST"])
def actualizar(id):
    collection.update_one(
        {"id": id},
        {"$set": {
            "nombre": request.form['nombre'],
            "jugadores_min": request.form['jugadores_min'],
            "jugadores_max": request.form['jugadores_max'],
            "edad": request.form['edad'],
            "pais": request.form['pais'],
            "costo": request.form['costo']
        }}
    )
    return redirect('/')

# Run
if __name__ == '__main__':
    app.run(debug=True)