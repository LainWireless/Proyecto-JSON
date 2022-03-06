import json
import os
def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def leer_libreria():
    try:
        f=open("libreria.json")
        datos = json.load(f)
        f.close()
        return datos
    except:
        print("Error al leer archivo .json")

def f_listar_datosbase(datos):
    lista1 = []
    lista2 = []
    nombrebase = datos.get("name")
    comandante = datos.get("garrison").get("commander").get("name")
    for instalaciones in datos.get("facilities"):
        lista1.append(instalaciones)
    for personal in datos.get("garrison").get("personnel"):
        lista2.append(personal)
    print("Nombre de la Base: ",nombrebase)
    print("Comandante: ",comandante)
    print("Instalaciones: ",lista1)
    print("Personal: ",lista2)
    
def f_contar_naves(datos):
    cont1 = len(datos.get("vehicle_assets"))
    cont2 = len(datos.get("starship_assets"))
    cont3 = len(datos.get("visiting_starships"))
    contt = cont1+cont2+cont3
    print("Hay ",contt," tipos de naves.")

def f_buscar_especie_genero(datos):
    #ubicación de los datos Droid
    dato1 = datos.get("evacuation_plan").get("transport_assignments")[0]
    dato2 = dato1.get("passenger_manifest")[1].get("species")[0].get("name")
    dato3 = dato1.get("escorts")[0].get("astromech_droid").get("species")[0].get("name")
    dato4 = dato1.get("escorts")[1].get("astromech_droid").get("species")[0].get("name")
    #ubicación del dato wookiee
    dato5 = datos.get("visiting_starships").get("freighters")[0].get("copilot").get("species")[0].get("name")
    #ubicaión de los datos human
    dato6 = datos.get("garrison").get("commander").get("species")[0].get("name")
    dato7 = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("species")[0].get("name")
    dato8 = datos.get("visiting_starships").get("freighters")[1].get("pilot").get("species")[0].get("name")
    dato9 = dato1.get("passenger_manifest")[0].get("species")[0].get("name")
    dato10 = dato1.get("escorts")[0].get("pilot").get("species")[0].get("name")
    dato11 = dato1.get("escorts")[1].get("pilot").get("species")[0].get("name")
    #ubicación de los datos male
    genero1 = datos.get("garrison").get("commander").get("gender")
    genero2 = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("gender")
    genero3 = datos.get("visiting_starships").get("freighters")[1].get("pilot").get("gender")
    genero4 = dato1.get("escorts")[0].get("pilot").get("gender")
    genero5 = dato1.get("escorts")[1].get("pilot").get("gender")
    #ubicación de los datos female
    genero6 = dato1.get("passenger_manifest")[0].get("gender")
    
    especie = input("\nEscriba la especie: ")
    if especie == dato2 and especie == dato3 and especie == dato4:
       nombre1 = dato1.get("passenger_manifest")[1].get("name")
       nombre2 = dato1.get("escorts")[0].get("astromech_droid").get("name")
       nombre3 = dato1.get("escorts")[1].get("astromech_droid").get("name")
       print(nombre1,", ",nombre2,", ",nombre3)
    elif especie == dato5:
        nombre = datos.get("visiting_starships").get("freighters")[0].get("copilot").get("name")
        print(nombre)
    elif especie == dato6 and especie == dato7 and especie == dato8 and especie == dato9 and especie == dato10 and especie == dato11:
        genero = input("\nEscriba el genero: ")
        if genero == genero1 and genero == genero2 and genero == genero3 and genero == genero4 and genero == genero5:
            nombre1 = datos.get("garrison").get("commander").get("name")
            nombre2 = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("name")
            nombre3 = datos.get("visiting_starships").get("freighters")[1].get("pilot").get("name")
            nombre4 = dato1.get("escorts")[0].get("pilot").get("name")
            nombre5 = dato1.get("escorts")[1].get("pilot").get("name")
            print(nombre1,", ",nombre2,", ",nombre3,", ",nombre4,", ",nombre5)
        elif genero == genero6:
            nombre = dato1.get("passenger_manifest")[0].get("name")
            print(nombre)
        else:
            print("\nParece que se ha equivocado, los dos géneros exietentes para los humanos son male y female.")    
    else:
       print("\nParece que se ha equivocado, las especies existentes son Human, Droid y Wookiee.")
       
def f_buscar_navepiloto(datos):
    dato1 = datos.get("evacuation_plan").get("transport_assignments")[0]
    Luke = dato1.get("escorts")[0].get("pilot").get("name")
    Wedge = dato1.get("escorts")[1].get("pilot").get("name")
    Solo = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("name")
    Dash = datos.get("visiting_starships").get("freighters")[1].get("pilot").get("name")
    nombrepiloto = input("\nEscribe el nombre del piloto: ")
    if Luke == nombrepiloto:
        print("Clase: ",dato1.get("escorts")[0].get("starship_class")," | Nombre: ",dato1.get("escorts")[0].get("name")," | Modelo: ",dato1.get("escorts")[0].get("model"))
    elif Wedge == nombrepiloto:
        print("Clase: ",dato1.get("escorts")[1].get("starship_class")," | Nombre: ",dato1.get("escorts")[1].get("name")," | Modelo: ",dato1.get("escorts")[1].get("model"))
    elif Solo == nombrepiloto:
        print("Clase: ",datos.get("visiting_starships").get("freighters")[0].get("starship_class")," | Nombre: ",datos.get("visiting_starships").get("freighters")[0].get("name")," | Modelo: ",datos.get("visiting_starships").get("freighters")[0].get("model"))
    elif Dash == nombrepiloto:
        print("Clase: ",datos.get("visiting_starships").get("freighters")[1].get("starship_class")," | Nombre: ",datos.get("visiting_starships").get("freighters")[1].get("name")," | Modelo: ",datos.get("visiting_starships").get("freighters")[1].get("model"))
    else:
        print("\nParece que se ha equivocado, los pilotos existentes son Luke Skywalker, Wedge Antilles, Dash Rendar y Han Solo.")
        
def f_listar_datosplaneta(datos):
    Hoth = datos.get("location").get("planet").get("name")
    Alderaan = datos.get("garrison").get("commander").get("homeworld").get("name")
    Corellia = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("homeworld").get("name")
    Tatooine = datos.get("evacuation_plan").get("transport_assignments")[0].get("passenger_manifest")[1].get("homeworld").get("name")
    Naboo = datos.get("evacuation_plan").get("transport_assignments")[0].get("escorts")[0].get("astromech_droid").get("homeworld").get("name")
    print("PLANETAS DISPONIBLES:")
    print(Hoth)
    print(Alderaan)    
    print(Corellia)    
    print(Tatooine)    
    print(Naboo)    
    nombreplaneta = input("\nEscribe el nombre del planeta: ")
    if nombreplaneta == Hoth:
        clima = datos.get("location").get("planet").get("climate")[0]
        terreno = list(datos.get("location").get("planet").get("terrain"))
        poblacion = datos.get("location").get("planet").get("population")
        print("Clima: ",clima," | Terreno: ",terreno," | Población: ",poblacion)
    elif nombreplaneta == Alderaan:
        clima = datos.get("garrison").get("commander").get("homeworld").get("climate")[0]
        terreno = list(datos.get("garrison").get("commander").get("homeworld").get("terrain"))
        poblacion = datos.get("garrison").get("commander").get("homeworld").get("population")
        print("Clima: ",clima," | Terreno: ",terreno," | Población: ",poblacion)
    elif nombreplaneta == Corellia:
        clima = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("homeworld").get("climate")[0]
        terreno = list(datos.get("visiting_starships").get("freighters")[0].get("pilot").get("homeworld").get("terrain"))
        poblacion = datos.get("visiting_starships").get("freighters")[0].get("pilot").get("homeworld").get("population")
        print("Clima: ",clima," | Terreno: ",terreno," | Población: ",poblacion)
    elif nombreplaneta == Tatooine:
        clima = datos.get("evacuation_plan").get("transport_assignments")[0].get("passenger_manifest")[1].get("homeworld").get("climate")[0]
        terreno = list(datos.get("evacuation_plan").get("transport_assignments")[0].get("passenger_manifest")[1].get("homeworld").get("terrain"))
        poblacion = datos.get("evacuation_plan").get("transport_assignments")[0].get("passenger_manifest")[1].get("homeworld").get("population")
        print("Clima: ",clima," | Terreno: ",terreno," | Población: ",poblacion)
    elif nombreplaneta == Naboo:
        clima = datos.get("evacuation_plan").get("transport_assignments")[0].get("escorts")[0].get("astromech_droid").get("homeworld").get("climate")[0]
        terreno = list(datos.get("evacuation_plan").get("transport_assignments")[0].get("escorts")[0].get("astromech_droid").get("homeworld").get("terrain"))
        poblacion = datos.get("evacuation_plan").get("transport_assignments")[0].get("escorts")[0].get("astromech_droid").get("homeworld").get("population")
        print("Clima: ",clima," | Terreno: ",terreno," | Población: ",poblacion)
    else:
        print("\nParece que se ha equivocado, los planetas disponibles no coinciden con el que ha tratado de buscar.")