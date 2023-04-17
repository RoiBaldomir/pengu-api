from fastapi import APIRouter, status
from db.client import db_client # Conexión con la BBDD
from db.models.penguin import Penguin # Importo el modelo
from db.schemas.penguin import penguin_schema, penguins_schema # Importo las funciones para estructurar los datos y poder devolverlos correctamente


router = APIRouter(prefix="/penguins",
                   tags=["penguins"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


def search_penguin(field: str, key): # Para filtrar los elementos según su campo y clave
    
    try:
        penguin = db_client.penguins.penguin_species.find_one({field: key})
        return Penguin(**penguin_schema(penguin))
    except:
        return {"error": "No existe la especie"}
    

@router.get("/", response_model=list[Penguin]) # Esta ruta devuelve la lista de especies de pingüinos
async def penguin():
    return penguins_schema(db_client.penguins.penguin_species.find())
    
@router.get("/{id}") # Esta ruta devuelve los datos de la especie del ID correspondiente
async def penguin(id: int):
    return search_penguin("id", id)