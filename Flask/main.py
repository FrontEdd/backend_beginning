from flask import Flask

app = Flask(__name__) # main.py

users = [
    {
        "id": 1,
        "name": "Andres",
        "last_name": "Taboada"
    },
    {
        "id": 2,
        "name": "Roberto",
        "last_name": "Quiroga"
    }
]

@app.route('/', methods=['GET'])
def index():
    return {
        'message': 'Hello world !'
    }

@app.route('/users', methods=['GET'])
def userList():
    return users, 200

#Path-Params:
#   string
#   int
#   float
#   path
#   uuid -> Identificador unico universal
@app.route('/users/<int:id>', methods=['GET'])
def userGetById(id):
    for user in users:
        if user['id'] == id:
            return user, 200

    return {
        'message': 'El usuario ingresado no existe'
    }, 404