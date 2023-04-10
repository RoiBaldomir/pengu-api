from fastapi import APIRouter, HTTPException, status
from data import penguin_data # Permite traer los datos de las especies


router = APIRouter()


def get_penguin(id): # Esta función sirve para filtrar las especies por su ID, devuelve una excepción si el id es incorrecto o no existe
    penguins = filter(lambda penguin: penguin.id == id, penguin_data.penguin_list)
    try:
        return list(penguins)[0]
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Especie no encontrada")


@router.get("/penguins") # Esta ruta devuelve la lista de especies de pingüinos
async def penguin():
    return penguin_data.penguin_list

@router.get("/penguins/{id}") # Esta ruta devuelve los datos de la especie del ID correspondiente
async def penguin(id: int):
    return get_penguin(id)