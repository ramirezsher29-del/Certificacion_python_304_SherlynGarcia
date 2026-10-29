#Mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#Recoriendo la matriz con ciclos anidados
#Ciclo externo para manejar filas(i)
for i in range(filas):
    #Ciclo externo para manejar columnas(j)
    for j in range(columnas):
        #Verificamos si encontramos el tesoro
        if mapa[i][j]=="X":
             print(f"Mapa encontraron en la posicion [{i}][{j}]")


