from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)

# Conexión local a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["juegos_db"]
collection = db["juegos"]

# Crear índice único por campo 'id'
collection.create_index("id", unique=True)

# ⚠️ DESARROLLO: Eliminar todos los datos si querés empezar de cero
# collection.delete_many({})

# Ruta principal - muestra los juegos
@app.route('/')
def index():
    juegos = list(collection.find())
    return render_template("index.html", juegos=juegos)

# Ruta del formulario para agregar un nuevo juego
@app.route('/form')
def form():
    return render_template("form.html")

# POST de JUEGO
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


# DELETE
@app.route('/eliminar/<int:id>', methods=["POST"])
def eliminar(id):
    collection.delete_one({"id": id})
    return redirect('/')

# PATCH
@app.route('/editar/<int:id>')
def editar(id):
    juego = collection.find_one({"id": id})
    if not juego:
        return "Juego no encontrado", 404
    return render_template("editar.html", juego=juego)


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


if __name__ == '__main__':
    app.run(debug=True)