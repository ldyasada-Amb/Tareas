# leer el archivo las frases que estan
def lectura():
    archivo = open('frases','r')
    oracion = archivo.read()
    print(oracion)
    archivo.close()

def escritura(texto):     # agrega frases dentro del archivo
    archivo = open('frases','a')
    archivo.write(texto)
    archivo.close()

while True:     # bucle para llamar a las diferentes funciones
    print("Bienvenido")
    print("Menu de opciones")
    print("1 lectura")
    print("2 escritura")
    print("3 salir")
    opcion = int(input("ingrese la opcion"))
    if opcion == 1:
        lectura()
    elif opcion == 2:
        texto = input("ingrese la frase")
        escritura(texto)
    elif opcion == 3:
        print("gracias por la atencion")
        break
    else:
        print("opcion no valida")



    




    
