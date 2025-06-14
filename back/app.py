from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)

# Conexión a MongoDB (por ahora local, más adelante con Docker Compose)
client = MongoClient("mongodb://localhost:27017/")
db = client["juegos_db"]
collection = db["juegos"]

# Crear índice único por _id (si no existe)
collection.create_index("id", unique=True)


# Renderizamos ambos HTML: 
@app.route('/')
def index():
    juegos = list(collection.find())
    return render_template("index.html", juegos=juegos)

@app.route('/form')
def form():
    return render_template("form.html")


# Ruta para POST
@app.route('/agregar', methods=["POST"])
def agregar():
    ultimo = collection.find_one(sort=[("_id", -1)])
    nuevo_id = str(int(ultimo["_id"]) + 1) if ultimo else "1"
    juego = {
        "_id": nuevo_id,
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
    
if __name__ == '__main__':
    app.run(debug=True)
