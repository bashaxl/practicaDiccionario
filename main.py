opMenu = 0
persona = {
    "Nombre":[],
    "Edad": [],
    "Apellido": [],
    "CI": []
}

while opMenu != 5:
    print("Practica de Diccionario")
    print("Este programa toma los datos: nombre, edad, apellido y C.I para luego guardarlos en diccionarios donde puedes:")
    print("1. Mostrar datos")
    print("2. Añadir datos")
    print("3. Modificar datos")
    print("4. Eliminar datos")
    print("5. Salir del menu")
    opMenu = int(input("Porfavor, escoja una opción\n"))
    if opMenu == 1:
        for key, valor in persona.items():
            print(key, valor)
            print("")
    elif opMenu == 2:
        print("¿Que dato deseas añadir?")
        print("1. Nombre")
        print("2. Edad")
        print("3. Apellido")
        print("4. CI")
        opEditar = int(input("Porfavor, escoja una opción.\n"))
        if opEditar == 1:
            persona['Nombre'].append(input("Ingrese el nombre: \n"))
        elif opEditar == 2:
            persona['Edad'].append(input("Ingrese la edad: \n"))
        elif opEditar == 3:
            persona['Apellido'].append(input("Ingrese el apellido: \n"))
        elif opEditar == 4:
            persona['CI'].append(input("Ingrese la CI: \n"))
        else:
            print("Porfavor, escoja una opción valida.\n")
    elif opMenu == 3:
        print("a")
    elif opMenu == 4:
        print("b")
    elif opMenu == 5:
        print("¡Gracias por probar mi programa!\n")
    else:
        print("Porfavor, escoja una opción valida.\n")

# El codigo se encuentra incompleto, ¡Ando trabajando en eso! :)
