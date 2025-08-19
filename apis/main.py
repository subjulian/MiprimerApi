from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/saludo/{nombre}")
def get_saludo(nombre: str):
    return {"Hello": nombre}