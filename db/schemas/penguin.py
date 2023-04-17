# Estructuro los datos recibidos de la BBDD para poder devolverlos sin problemas

def penguin_schema(penguin) -> dict:
    return {"id": penguin["id"],
            "penguin_species": penguin["name"],
            "height_cm": penguin["height_cm"],
            "weight_kg": penguin["weight_kg"],
            "habitat": penguin["habitat"],
            "description": penguin["description"]}

# Para devolver todos las estructuras en una lista y así poder ver la lista de especies al completo

def penguins_schema(penguins) -> list:
    return [penguin_schema(penguin) for penguin in penguins]