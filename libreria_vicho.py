#ejercicio tipo prueba libreria
import os, json, time
from Funciones_B import *
while True:
    print("\tBIBLIOTECA ")
    print("1.Agregar libro")
    print("2.Mostrar libros")
    print("3.buscar libro por titulo")
    print("4.Actualizar info")
    print("5.Guardar libro (json)")
    print("6.salir")
    opc = int(input("ingrese una opcion: "))
    if opc == 1:
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc == 3:
        opcion_3()
    elif opc == 4:
        opcion_4()
    elif opc == 5:
        opcion_5()
    elif opc == 6:
        opcion_6()
    time.sleep(3)
    
   
        
        
        

