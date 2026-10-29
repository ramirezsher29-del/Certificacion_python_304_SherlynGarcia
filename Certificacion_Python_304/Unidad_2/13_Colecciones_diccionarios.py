#Creando diccionario
persona={
    "Nombre":"Sherlyn",
    "Edad":16,
    "Profesion":"Programador",
    "Estudiante":False
}
print(persona)
#Accediendo a un valor especifico
print(persona["Nombre"])
print(persona.get("Profesion"))
persona["Edad"]=18
print(persona["Edad"])
persona["Ciudad"]="San pepe ranch"
print(persona)
for clave,valor in persona.items():
    print(f"{clave}:{valor}")