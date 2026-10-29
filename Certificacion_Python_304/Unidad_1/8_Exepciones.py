#Ejemplo 1 sin manejo de exepciones
try:
    numero1=float(input("Ingresa el primer numero:"))
    numero2=float(input("Ingresa el segundo numero:"))
    numero1=10
    numero2=5
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError,ValueError:
    print("Error no se puede ingresar una letra")