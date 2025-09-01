matriz = [
[1,2,3],
[2,4,5],
[3,7,8]
]

print(matriz)
for filas in matriz:
    for columnas in filas:
        if columnas == 8:
            print("Si existe el numero 8 en la matriz")

#Encuentra el numero                       
numero = 8

for i, fila in enumerate(matriz):
    if numero in fila:
        j = fila.index(numero)
        print(f"El número {numero} está en la fila {i} y columna {j}")
        break
                  
                  

