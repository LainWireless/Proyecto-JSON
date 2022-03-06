from funciones import *

libreria = leer_libreria()

menu = '''MENU
1. Listar nombre de la base, comandante, instalaciones y personal.
2. Contar cuantos tipos de vehiculos y naves hay en la base base.
3. Mostrar nombre de personajes a partir de su especie y género.
4. Busca nombre de un personaje que sea piloto y te muestra el tipo de nave, el nombre de su nave y el modelo.
5. Elige un planeta para ver su clima, terreno y población.
0. Salir\n'''

clear()
print(menu)
vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
try:
    opcion = int(vopcion)
except:
    opcion = 6
    
while opcion != 0:
    if opcion == 1:
        print()
        f_listar_datosbase(libreria)
        input("\nListado completado. Pulsar ENTER para volver al menú principal.")
        clear()
        print(menu)
        vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
        try:
            opcion = int(vopcion)
        except:
            opcion = 6
    elif opcion == 2:
        print()
        f_contar_naves(libreria)
        input("\nListado completado. Pulsar ENTER para volver al menú principal.")
        clear()
        print(menu)
        vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
        try:
            opcion = int(vopcion)
        except:
            opcion = 6
    elif opcion == 3:
        print()
        f_buscar_especie_genero(libreria)
        input("\nListado completado. Pulsar ENTER para volver al menú principal.")
        clear()
        print(menu)
        vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
        try:
            opcion = int(vopcion)
        except:
            opcion = 6
    elif opcion == 4:
        print()
        f_buscar_navepiloto(libreria)
        input("\nListado completado. Pulsar ENTER para volver al menú principal.")
        clear()
        print(menu)
        vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
        try:
            opcion = int(vopcion)
        except:
            opcion = 6
    elif opcion == 5:
        print()
        f_listar_datosplaneta(libreria)
        input("\nListado completado. Pulsar ENTER para volver al menú principal.")
        clear()
        print(menu)
        vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
        try:
            opcion = int(vopcion)
        except:
            opcion = 6
    else:
        input("Opción inválida. Pulsa cualquier tecla para volver al menú principal.")
        clear()
        print(menu)
        vopcion = input("\nEscriba el número correspondiente a la opción elegida: ")
        try:
             opcion = int(vopcion)
        except:
            opcion = 6
if opcion == 0:
    print()
    print("Adios.")