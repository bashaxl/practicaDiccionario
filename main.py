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
    opMenu = int(input("Porfavor, escoja una opción: "))
    if opMenu == 1:
        # Parte de mostrar datos
        for key, valor in persona.items():
            print(f"\n{key} || {valor}\n")
    elif opMenu == 2:
        # Parte de añadir datos
        print("¿Que dato deseas añadir?")
        print("1. Nombre")
        print("2. Edad")
        print("3. Apellido")
        print("4. CI")
        opEditar = int(input("Porfavor, escoja una opción: "))
        if opEditar == 1:
            # Esta variable es la que usaré para el while de este apartado.
            tempOpMenu = 0
            # Esta es la variable que voy a usar para el tema de confirmar, guardaré el dato, preguntaré y luego cambiaré
            tempInput = input("Ingrese el nombre: ")
            while tempOpMenu != 1:
                print("\n ¿Estas seguro/a de querer realizar los cambios? \n")
                print("1. Sí, estoy seguro")
                print("2. No, no estoy seguro")
                print("3. Cancelar")
                tempOpMenu = int(input("Porfavor, escoja una opción: "))
                if tempOpMenu == 1:
                    print("¡Dato añadido con exito!")
                    persona['Nombre'].append(tempInput)
                elif tempOpMenu == 2:
                    tempInput = input("Ingrese el nombre: ")
                elif tempOpMenu == 3:
                    break
                else:
                    print("Porfavor, introduzca un valor valido.")
            # Como dice en el archivo "notas" en la hora 21:18 (17/05/2025), logré implementar mi solución. Ahora solo queda repetir la logica.
        elif opEditar == 2:
            tempOpMenu = 0
            tempInput = int(input("Ingrese la edad: "))
            while tempOpMenu != 1:
                print("\n ¿Estas seguro/a de querer realizar los cambios? \n")
                print("1. Sí, estoy seguro")
                print("2. No, no estoy seguro")
                print("3. Cancelar")
                tempOpMenu = int(input("Porfavor, escoja una opción: "))
                if tempOpMenu == 1:
                    print("¡Dato añadido con exito!")
                    persona['Edad'].append(tempInput)
                elif tempOpMenu == 2:
                    tempInput = int(input("Ingrese la edad: "))
                elif tempOpMenu == 3:
                    break
                else:
                    print("Porfavor, introduzca un valor valido.")
        elif opEditar == 3:
            tempOpMenu = 0
            tempInput = input("Ingrese el apellido: ")
            while tempOpMenu != 1:
                print("\n ¿Estas seguro/a de querer realizar los cambios? \n")
                print("1. Sí, estoy seguro")
                print("2. No, no estoy seguro")
                print("3. Cancelar")
                tempOpMenu = int(input("Porfavor, escoja una opción: "))
                if tempOpMenu == 1:
                    print("¡Dato añadido con exito!")
                    persona['Apellido'].append(tempInput)
                elif tempOpMenu == 2:
                    tempInput = input("Porfavor, ingrese el apellido: ")
                elif tempOpMenu == 3:
                    break
                else: 
                    print("Porfavor, introduzca un valor valido.")
        elif opEditar == 4:
            tempOpMenu = 0
            tempInput = int(input("Ingrese la Cedula de Identidad: "))
            while tempOpMenu != 1:
                print("\n ¿Estas seguro/a de querer realizar los cambios? \n")
                print("1. Sí, estoy seguro")
                print("2. No, no estoy seguro")
                print("3. Cancelar")
                tempOpMenu = int(input("Porfavor, escoja una opción: "))
                if tempOpMenu == 1:
                    print("¡Dato añadido con exito!")
                    persona['CI'].append(tempInput)
                elif tempOpMenu == 2:
                    tempInput = int(input("Porfavor, ingrese la C.I: "))
                elif tempOpMenu == 3:
                    break
                else:
                    print("Porfavor, introduzca un valor valido.")
        else:
            print("Porfavor, escoja una opción valida. \n")
    elif opMenu == 3:
        # Parte de modificar datos
        print("a")
    elif opMenu == 4:
        # Parte de eliminar datos
        print("b")
    elif opMenu == 5:
        # Parte de cerrar programa
        print("¡Gracias por probar mi programa!\n")
    else:
        # Mensaje de error
        print("Porfavor, escoja una opción valida.\n")

# El código sigue incompleto, ¡ando trabajando en eso! :)