import random
import csv
import os
trabajadores=[
    "juan perez",
    "maria garcia",
    "carlos López",
    "ana martinez",
    "pedro rodriguez",
    "Laura hernandez",
    "miguel sanchez",
    "isabel gomez",
    "francisco diaz",
    "elena fernandes"
]
sueldo_trabajadores=[]
with open("sueldos_trabajadores.csv","w") as archivo:
    archivo.write("nombre   sueldobase    desc salud    descuento afp    sueldo liquido\n")
def sueldos_aleatorios():
    for numero in range(len(trabajadores)):
        sueldo_trabajadores.append({"nombre":trabajadores[numero],"sueldo":random.randint(300000,2500000)})
    return "finalizado"

def clasificar_sueldos():
    pass
def estadistica():
    producto=1
    total=0
    personas_ordenadas=sorted(sueldo_trabajadores, key=lambda x :x["sueldo"])
    print("1)mostrar sueldo mas alto")
    print("2)mostrar sueldo mas bajo")
    print("3)mostrar promedio de sueldos")
    print("4)mostrar medio geometrica")
    while True:
        try:
            opcion=int(input("ingrese una opcion: "))
        except ValueError:
            print("SOLO DEBES INGRESAR VALORES NUMERICOS")
        else:
            match opcion:
                case 1:
                    print(max(personas_ordenadas,key=lambda x:x[sueldo_trabajadores]))
                case 2: 
                    print(min(personas_ordenadas, key=lambda x:x[sueldo_trabajadores]))
                case 3:
                    for sueldo in sueldo_trabajadores:
                        sueldo_trabajadores=sueldo**1/10
                    
                    
def reporte_de_sueldos():
    if len(sueldo_trabajadores)==0:
        print("no se encontro registro de sueldos")
        input()
        return
    with open("sueldos_trabajadores.csv", "w",newline="") as archivo:
        print("nombre \tsueldo base\tdescuento afp\tsueldo liquido")
        escribir=csv.write(archivo)
        escribir.write(["nombre ", "sueldo base", "descuento afp", "sueldo liquido"])
        for a in sueldo_trabajadores:
            des_salud=int(a["sueldo"]*0.07)
            desc_afp=int(a["sueldo"]*0.12)
                                
                        
while True:
    print("1)ASIGNAR SUELDOS ALEATORIOS")
    print("2)CLASIFICAR SUELDOS")
    print("3)VER ESTADISTICA")
    print("4)REPORTE DE SUELDOS")
    print("5)SALIR DEL PROGRAMA")
    while True:
        try:
            op=input("ingrese la opcion que desea: ")
        except ValueError:
            print("solo debe ingresar valores numericos")
        else:
            match op:
                case "1":
                    sueldos_aleatorios()
                case 2:
                    pass
                case "3":
                    estadistica() 
                case 4:
                    pass   
                case 5:
                    print("finalizando programa / desarrollado por Dayelin Benavides  / rut: 21.171.554-5    ")
