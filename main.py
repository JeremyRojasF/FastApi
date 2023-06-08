from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    return 'Hello World'

@app.get('/login')
def mensaje():
    return 'Inicie sesion'


@app.get('/users')
def mensaje():
    users=[
        {
            "nombre": "Pablo",
            "apellido": "España"
        }
    ]
    return users


@app.get('/auth/login/users')
def mensaje():
    users=[
        {
            "nombre": "Pablo",
            "apellido": "España"
        }
    ]
    return users