# Separar los nombres en grupos

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["Messi", "Pele", "Juanes"]

#creacion de la lista completa 

lista = (magos, cientificos, otros)

# Función para hacer_grandiosos a los magos

def hacer_grandioso(magos, frase):
    return [f"{frase} {nombre}" for nombre in magos]

#Definicion de la frase y variable
frase = "El Gran"
nombres_con_frase = hacer_grandioso(magos, frase)
print("Imprimir la  funcion ---------- Hacer grandioso----------------")
print(nombres_con_frase)
print("Separacion 1 funcion --------------------------")

# Función para imprimir los nombres
def imprimir_nombres():
    for nombre in lista:
        print(nombre)

print("Separacion ---------LLama a la funcion Imprimir Nombres de la lista-----------------")
# Llamada a la función
imprimir_nombres()  

print("Separacion 2 funcion --------------------------")
print("imprimio a los cientificos")
print(cientificos)
print("imprimio a los magos")
print(magos)
print("imprimio a los otros")
print(otros)

