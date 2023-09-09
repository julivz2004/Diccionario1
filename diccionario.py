animales = {}

def llenar_informacion():
    nombre = input('Nombre del animal: ')
    edad = input('Edad del animal: ')
    
    if nombre == 'perro' or nombre == 'gato':
        raza_o_especie = input('Raza del animal: ')
    else:
        raza_o_especie = input('Especie del animal: ')
    
    animales[nombre] = {'nombre': nombre, 'edad': edad}
    
    if nombre == 'perro' or nombre == 'gato':
        animales[nombre]['raza'] = raza_o_especie
    else:
        animales[nombre]['especie'] = raza_o_especie

def imprimir_informacion():
    for nombre_animal, info_animal in animales.items():
        print(f'Animal: {nombre_animal}')
        for clave, valor in info_animal.items():
            print(f'{clave}: {valor}')
        print()

def eliminar_animal():
    nombre = input('Nombre del animal a eliminar: ')
    if nombre in animales:
        del animales[nombre]
        print(f'{nombre} ha sido eliminado.')
    else:
        print(f'{nombre} no se encuentra en la lista de animales.')

def editar_animal():
    nombre = input('Nombre del animal a editar: ')
    if nombre in animales:
        print(f'Editar información de {nombre}:')
        llenar_informacion()
    else:
        print(f'{nombre} no se encuentra en la lista de animales.')

while True:
    print("\nMenú:")
    print("1. Llenar información de un animal")
    print("2. Imprimir información de todos los animales")
    print("3. Eliminar un animal")
    print("4. Editar la información de un animal")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        llenar_informacion()
    elif opcion == "2":
        imprimir_informacion()
    elif opcion == "3":
        eliminar_animal()
    elif opcion == "4":
        editar_animal()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
