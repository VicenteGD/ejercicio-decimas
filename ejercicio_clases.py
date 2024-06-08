from funciones import *

import csv
import os
os.system("cls")

personas=[]

while True:
    
    nombre()
    apellido()
    edad()
     
    print("persona agregada con éxito: ")
        
    personas.append(nombre)
    personas.append(apellido)
    personas.append(edad)
    
    si_no=input("desea continuar? SI/NO: ")
    if si_no.lower()=="si":
        pass
        
    else:
        print("personas agregadas con exito! ")
        print(personas)
        break
    
    archivo(personas)

    




