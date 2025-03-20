users = [
    [
        ("Nombre", "Nicolas"),
        ("Apellido", "Stasyszyn Parisi"),
        ("Edad", "17"),
        ("Nacionalidad", "Argentia"),
        ("Genero", "Hombre"),
    ],
    [
        ("Nombre", "Emma"),
        ("Apellido", "Stasyszyn Parisi"),
        ("Edad", "14"),
        ("Nacionalidad", "Argentia"),
        ("Genero", "Mujer"),
    ],
]
a = 0
for i in users:
    print("-----------")

    for x in i:
        print(x[1])
print("-----------")
