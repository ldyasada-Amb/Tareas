matriz = [
    [1,3,2],
    [5,4,6],
    [9,8,7]
]

print(matriz)
for j in range(len(matriz)): # Imprime la matriz rdenada
    matriz[j].sort()
print(matriz)

print("-"*30)

print(matriz)
for j in range(len(matriz)): # Imprime la matriz rdenada
    for h in range(len(matriz)):
        (matriz[h]).sort()
print(matriz[j][h])

       
     
