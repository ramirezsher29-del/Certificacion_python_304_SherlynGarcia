carrito=[]#Lista vacia
n_productos=int(input("ingresa el número de productos"))
for i in range(n_productos):
    producto=input("ingresa el producto a tu carrito")
    carrito.append(producto)
print("Lista creada correctamente")    
carrito[0]="barritas"
print(carrito[0])
print(carrito[1])
print(carrito)