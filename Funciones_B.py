import os, json, time

estante= []
def opcion_1():
    os.system("cls")
    titulo =input("ingrese el tutulo del libro: ")
    autor = input("ingrese nombre del autor: ")
    anio= int(input("ingrese año del libro: "))
    genero= input("ingrese el genero del libro: ")
    print("Libro agregado con exito")
    libro={
        "titulo":titulo,
        "autor":autor,
        "anio":anio,
        "genero":genero
    }
    estante.append(libro)

def opcion_2():
    os.system("cls")
    if len(estante)==0:
        print("No se a guardado ningun libro")
    else:
        print("\tLista de libros guardados")
        for lulo in estante:
            print(f"Titulo: {lulo['titulo']}, Autor: {lulo['autor']}, Anio: {lulo['anio']}, Genero: {lulo['genero']}")

def opcion_3():
    busqueda = input("Ingrese el nombre del libro que desea buscar: ")
    libro_encontrado = None
    for vicho in estante:
        if vicho["titulo"].lower() == busqueda.lower():
            libro_encontrado = vicho
            
    if libro_encontrado:
        print("Libro encontrado:")
        print(f"Título: {libro_encontrado['titulo']}")
        print(f"Autor: {libro_encontrado['autor']}")
        print(f"Año: {libro_encontrado['anio']}")
        print(f"Género: {libro_encontrado['genero']}")
    else:
        print("El libro no se ha encontrado!!")
    
def opcion_4():
    busqueda = input("Ingrese el nombre del libro que desea buscar: ")
    libro_encontrado = None
    for vicho in estante:
        if vicho["titulo"].lower() == busqueda.lower():
            libro_encontrado = vicho
            break

    if libro_encontrado:
        print("\nSe encontró el libro")
        nuevo_nom = input("Agregue nuevo nombre: ")
        nuevo_anio = input("Agregue nuevo año: ")
        nuevo_gen = input("Agregue nuevo género: ")
        if nuevo_nom:
            libro_encontrado["titulo"] = nuevo_nom
        if nuevo_anio:
            libro_encontrado["anio"] = int(nuevo_anio)
        if nuevo_gen:
            libro_encontrado["genero"] = nuevo_gen
            return  nuevo_nom, nuevo_anio, nuevo_nom
        print("Libro actualizado con éxito")
    else:
        print("No se encontró ningún libro con ese nombre")

                        
            
def opcion_5():
    with open("libros.json","w") as archivo:
        json.dump(estante, archivo)
        print("los datos de los libros fueron creado con exito")

    with open("libro.json","r") as archivo:
        libro_cargado = json.load(archivo)
        print(libro_cargado)
    
def opcion_6():
    print("gracias por usar el gestionamiento de libros")
    exit()
