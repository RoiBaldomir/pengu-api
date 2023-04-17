from pydantic import BaseModel


class Penguin(BaseModel): # Utilizo una clase para estructurar los datos de los pingüinos
    id: int
    penguin_species: str
    height_cm: int
    weight_kg: int
    habitat: str
    description: str