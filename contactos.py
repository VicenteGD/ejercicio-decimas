#ejercicio de lista de contactos!

import os, time
import csv


datos_contacto=[]

while True:
   
    
    print("""\tlista de contactos
    1). Agregar a contactos 
    2). Mostrar contactos
    3). Guardar contactos en archivo csv
    4). Salir""")

    while True:
        
        try:
            opc=int(input("ingrese un opción (1,2,3,4): "))
            if opc in (1,2,3,4):
                break
            else:
                print("error! ingrese una opción entre (1,2,3,4)!")
        except: 
            print("Error! ingrese un numero entero!")

    if opc ==1:
        os.system("cls")
        while True:
            
            print("agregar a contactos: ")
            nombre_apellido=input("ingrese nombre del nuevo contacto: ")
            if len(nombre_apellido) > 3: 
                break
            else:
                print("error! el nombre debe tener minimo 3 caracteres! ")
                
        while True:
            try:
                numero_telefonico=int(input("ingrese el número Telefonico del nuevo contacto: "))
                if numero_telefonico >= 9: 
                    break 
                else:
                    print("error! el numero debe tener minimo 9 numeros!")
            except:
                print("error! deben ser números enteros!")
        while True:
            correo=input("ingrese un correo electronico valido para el nuevo contacto: ")
            if len(correo)> 10:
                break
            else:
                print("error! debe tener minimo 10 caracteres!")
                
        contacto={
            "nombre_apellido":nombre_apellido,
            "numero":numero_telefonico,
            "correo":correo
            }
        datos_contacto.append(contacto)
        
        
        
    elif opc==2:
        os.system("cls")
        
        print("mostrar lista de contactos: ")
        for lulo in datos_contacto:
            print(f"nombre_apellido: {lulo['nombre_apellido']}\nNUMERO TELEFONICO: {lulo['numero']}\nCORREO ELECTRONICO: {lulo['correo']}") 
    
    elif opc==3:
        
            os.system("cls")
            
            print("guardar contactos en archivo csv ")
            while True:
                nombre_archivo= input("ingrese nombre del archivo : ")
                if len(nombre_archivo)>3:
                    break
                else:
                    print("error! ingrese nombre de un archivo existente!")
                    

                with open (f"{nombre_archivo}"+".csv", "a", newline="") as csvfile:
                    escritor= csv.writer(csvfile)
                    escritor.writerow(datos_contacto)
                
    
    else:
        print("Error!")
        
    
        


