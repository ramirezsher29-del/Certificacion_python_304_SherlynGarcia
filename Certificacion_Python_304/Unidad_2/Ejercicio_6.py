tabla=[
    ["Nombre","Edad","Calificacion"],
    ["Ivan",16,9],
    ["Cecilia",15,8],
    ["Mari",15,9],
    ["Jimena",16,7],
    ["Amanda",16,8],
    ["Litzi",15,8],
    ["Sherlyn",16,8],
    ["Ivon",16,9],
    ["Pedro",17,7],
    ["Sofia",16,6] 
]
nombre=input("Escribe tu nombre:")
filas=len(tabla)
columnas=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j]== nombre:
             print(f"Tu nombre esta en la posicion [{i}][{j}]")


