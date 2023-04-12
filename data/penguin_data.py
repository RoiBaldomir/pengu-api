from pydantic import BaseModel


class Penguin(BaseModel): # Utilizo una clase para estructurar los datos de los pingüinos
    id: int
    penguin_species: str
    height_cm: int
    weight_kg: int
    habitat: str
    description: str


penguin_list = [ # Lista con todos los datos de las especies de pingüinos
    Penguin(id = 1, penguin_species = "Pingüino emperador", height_cm = 120, weight_kg = 30, habitat ="Antártida", description = "El más grande de los pingüinos. Cada año, realizan un largo viaje para reproducirse."),
    Penguin(id = 2, penguin_species = "Pingüino rey", height_cm = 100, weight_kg = 16, habitat ="Chile, islas de América del Sur y África", description = "Un poco más pequeño que el emperador. La elección de pareja se basa en la viveza de la coloración del pelaje que es un reflejo de la salud del individuo"),
    Penguin(id = 3, penguin_species = "Pingüino de adelia", height_cm = 70, weight_kg = 4, habitat ="Antártida", description = "Se caracteriza porque su ojo posee un anillo blanco alrededor. La base del pico está oculta por unas plumas negras"),
    Penguin(id = 4, penguin_species = "Pingüino de barbijo", height_cm = 75, weight_kg = 5, habitat ="Antártida", description = "Tiene una línea negra bajo la barbilla que le da el nombre. Esta linea horizontal y el 'casco' negro de su cabeza lo hacen fácilmente diferenciable de otras especies similares"),
    Penguin(id = 5, penguin_species = "Pingüino papúa", height_cm = 85, weight_kg = 8, habitat ="Isla de Peterman, islas Malvinas y cerca de la Antártida", description = "Se caracterizan por poseer una mancha blanca en el ojo que se extiende hacia atrás. Contrasta con el resto de la cabeza y lomo que son completamente negros. Son los pinguinos más rápidos bajo el agua"),
    Penguin(id = 6, penguin_species = "Pingüino de las Galápagos", height_cm = 40, weight_kg = 5, habitat ="Islas Galápagos", description = "Es la única especie que vive en el hemisferio norte. Su número se ha visto reducido en las últimas décadas y se cree que quedan unos 2000 ejemplares aproximadamente"),
    Penguin(id = 7, penguin_species = "Pingüino de Humboldt", height_cm = 60, weight_kg = 5, habitat ="América del Sur", description = "Al igual que el pingüino de barbijo poseen una linea en la parte alta de su pecho pero es más ancha y con una curvatura mayor"),
    Penguin(id = 8, penguin_species = "Pingüino africano", height_cm = 75, weight_kg = 5, habitat ="África", description = "También se les conoce como pingüinos rallados por la linea de color negro que atraviesa su pecho. Estos pinguinos no soportan temperaturas muy bajas sino que le gustan más los ambientes cálidos"),
    Penguin(id = 9, penguin_species = "Pingüino de Magallanes", height_cm = 45, weight_kg = 3, habitat ="Chile, Argentina y las islas Malvinas", description = "Para diferenciarlo de otros pingüinos similares, hay que fijarse en las rayas de su pecho"),
    Penguin(id = 10, penguin_species = "Pingüino de penacho amarillo", height_cm = 55, weight_kg = 4, habitat ="Antártida", description = "Su cabeza negra, posee unas pobladas cejas con plumas amarillas y negras. Sus ojos son de color rojo"),
    Penguin(id = 11, penguin_species = "Pingüino macaroni", height_cm = 75, weight_kg = 5, habitat ="América del Sur y África", description = "Posee una cresta similar al pingüino de penacho amarillo pero con una coloración anaranjada"),
    Penguin(id = 12, penguin_species = "Pingüino real", height_cm = 70, weight_kg = 5, habitat ="Isla de Macquarie, Antártida", description = "Es muy parecido al pingüino macaroni pero su cara es blanca. Poseen también una cresta amarillo-anaranjada"),
    Penguin(id = 13, penguin_species = "Pingüino de Fiordland", height_cm = 60, weight_kg = 5, habitat ="Nueva Zelanda", description = "Su nombre se debe a que crían en la costa de Fiordland e islas cercanas. En lengua maorí lo conocen como 'tawaki'"),
    Penguin(id = 14, penguin_species = "Pingüino de cresta erecta", height_cm = 70, weight_kg = 4, habitat ="Nueva Zelanda", description = "Este pingüino posee una coloración muy viva. Su color es negro en el lomo y blanco en el vientre. En la cabeza posee 2 crestas de un amarillo brillante"),
    Penguin(id = 15, penguin_species = "Pingüino de Snares", height_cm = 55, weight_kg = 4, habitat ="Isla de Snares, Nueva Zelanda", description = "Es muy parecido al pingüino de Fiordland, se diferencia en que posee una región de piel de color rosado en la base de su pico"),
    Penguin(id = 16, penguin_species = "Pingüino de ojos amarillos", height_cm = 60, weight_kg = 8, habitat ="Nueva Zelanda", description = "Se caracterizan por poseer unos ojos amarillos de los que surge una linea amarillenta hacia la parte trasera de su cabeza"),
    Penguin(id = 17, penguin_species = "Pequeño pingüino azul", height_cm = 40, weight_kg = 1, habitat ="Nueva Zelanda, Australia, islas Chathan y Tasmania", description = "Se caracterizan además de por su tamaño, por su coloración. La parte dorsal es de tonalidades azules. El vientre es blanco"),
    Penguin(id = 18, penguin_species = "Pingüino enano de alas blancas", height_cm = 30, weight_kg = 2, habitat ="Nueva Zelanda", description = "Junto con el pingüino azul la especie de pingüinos más pequeña del mundo. Es por su tamaño y semejanzas con el pingüino azul que muchos consideran a este pingüino una subespecie de la anterior")]