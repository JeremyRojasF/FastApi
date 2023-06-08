from fastapi import FastAPI

app = FastAPI()

users = [
    {
        "id":1,
        "nombre": "Pablo",
        "apellido": "España",
        "edad": 26
    },
    {
        "id":2,
        "nombre": "José",
        "apellido": "Sanchez",
        "edad": 23
    }
]

@app.get("/")
def message():
    return 'Hello World'


@app.get('/users')
def mensaje():
    return users

@app.get('/user/{id}/edad/{edad}')
def get_user(id, edad):
    print(edad)
    for user in users:
        if user['id']== int(id) and user['edad'] == int(edad):
            return user
    return 'Usuario no encontrado'