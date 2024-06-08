import csv

personas=[]
def nombre():
    while True:
        nombre=input("ingrese su nombre: ")
        if len(nombre)>=3:
            return nombre
        else:
            print("error!, debe ingresar un nombre mayor a 2 caracteres!")
            
def apellido():
    while True:
        apellido=input("ingrese su apellido: ")
        if len (apellido) >=3:
            break
        else:
            print("error!, debe ingresar un apellido mayor a 2 caracteres!")
            
def edad():
    while True:
        try:
            edad=int(input("ingrese su edad: "))
            if edad > 0:
                break
            else:
                print("error! debe ingresar una edad existente!")
        except:
            print("Error! debe ingresar un numero entero!")
            
            
def archivo(personas):
    with open("archivo.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(personas)
    
            