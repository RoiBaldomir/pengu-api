from fastapi import FastAPI
from routers import penguins # Router pingüinos

app = FastAPI()

app.include_router(penguins.router) # Añado la ruta

@app.get("/") # Muestro un mensaje de bienvenida en la raíz de la API
async def root():
    return {"mensaje": "Bienvenido a PinguAPI: la API esencial para los amantes de los pingüinos"}