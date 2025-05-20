from fastapi import fastapi

app = FastAPI()

app.get("/")
def hola_mundo():
    return{"message": "Hola mundo, porfavor funciona"}
