Producto=input("Producto:")
Precio=float(input("Precio:"))
Cantidad=int(input("Cantidad:"))
total=Precio * Cantidad
print("Producto", Producto)
print("Total:", total)

nombres=["Mari","litzi","Ivan","Ivon","Jimena"]
calificaciones=[9.5,9,10,8,8.5]
for i in range(len(nombres)):
    if i % 2 ==0:
        print(i,nombres[i],calificaciones[i])