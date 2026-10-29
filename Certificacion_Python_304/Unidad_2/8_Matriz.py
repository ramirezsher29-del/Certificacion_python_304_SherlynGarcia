#Creando una matriz
numeros=[
    [1,2,3],#Fila 0
    [4,5,6],#Fila 1
    [7,8,9]# Fila 2
]
#Opteniendo el numero de filas 
#filas=len(numeros)#filas=3
#Opteniendo el numero de columnas
#columnas=len(numeros[0])
#Ciclo externo para los índices de las filas(i)
for i in range(0,3):
    #Ciclo interno para los indices de las columnas(j)
    for j in range(0,3):
        print(f"[{i}][{j}] = {numeros[i][j]}")

