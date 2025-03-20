# {
# "Titulo": "Destornillador",
# "Descripcion": "Ir a comprar un destornillador a la ferreteria"
# "Fecha_limite": "20 de diciembre"
# "Prioridad": "1"
# }

tasks = []
new = "si"
while new != "no":
    if new == "si":
        print("Ingrese el Titulo de la tarea:")
        title = input()
        print("----------")
        print("Ingrese la Descripcion de la tarea:")
        description = input()
        print("----------")
        print("Ingrese la Fecha Limite de la tarea:")
        last_day = input()
        print("----------")
        print("Ingrese el nivel de Prioridad de la tarea con un numero:")
        priority = input()
        print("----------")
        print("Agregar otra tarea si o no")
        new = input().lower()

        tasks.append(
            {
                "Titulo": title,
                "Prioridad": priority,
                "Descripcion": description,
                "Fecha_Limite": last_day,
            }
        )
    else:
        print("Respuesta invalida, ¿si o no?:")
        new = input().lower()

task = None
for i in tasks:
    task = i
    print(">------------------<")
    print("Prioridad:", task["Prioridad"])
    print("Titulo", task["Titulo"])
    print("Descripcion:", task["Descripcion"])
    print("Fecha_Limite:", task["Fecha_Limite"])