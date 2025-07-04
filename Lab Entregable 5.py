# Actividad 1. Uso de Python básico.

#PASO 1 SINTAXIS BASICA Y OPERACIONES SIMPLES: 
# A. Escribir un programa que imprima un mensaje en la consola.
print("¡Bienvenido al Laboratorio entregable No5 de Fundamentos de Python!")
print("For Jhon Steven Rojas Cadena")
print("----------------------------------------------------")

# B. Declarar variables de diferentes tipos y realizar operaciones matemáticas.
# Variables enteras (int)
numero_a = 25
numero_b = 10
# Variable de punto flotante (float)
precio = 99.95
# Variable de cadena de texto (str)
saludo = "Hola talento tech"
# Realizar operaciones matemáticas simples
suma = numero_a + numero_b
resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division = numero_a / numero_b # En Python, la división / siempre da un float
print(f"Operaciones con los números {numero_a} y {numero_b}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print("----------------------------------------------------")

# C. Concatenar cadenas de texto y utilizar funciones básicas como print() y input().
# Concatenación
nombre_usuario = input("Por favor, introduce tu nombre: ")
mensaje_bienvenida = saludo + ", " + nombre_usuario + "!"
print(mensaje_bienvenida)
# Uso de f-strings (una forma más moderna y legible de formatear cadenas)
edad_usuario_str = input("¿Cuántos años tienes? ")
# La función input() siempre devuelve una cadena (str), hay que convertirla si queremos usarla como número.
edad_usuario_int = int(edad_usuario_str) 
print(f"¡Genial, {nombre_usuario}! Entonces tienes {edad_usuario_int} años.")



#PASO 2 CONDICIONALES Y BUCLES
# A. Script para determinar si un número es par o impar (if/else)
try:
    numero_str = input("Introduce un número entero para saber si es par o impar: ")
    numero = int(numero_str)
    
    # El operador % (módulo) da el residuo de una división.
    # Si el residuo de dividir entre 2 es 0, el número es par.
    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")

except ValueError:
    print("Error: Debes introducir un número entero válido.")

print("----------------------------------------------------")

# B. Bucle 'for' para iterar sobre una lista y imprimir sus cuadrados
numeros_base = [2, 5, 8, 10, 13]
print(f"Calculando el cuadrado de los números en la lista: {numeros_base}")

for num in numeros_base:
    cuadrado = num ** 2  # El operador ** es para elevar a una potencia
    print(f"El cuadrado de {num} es {cuadrado}")

print("----------------------------------------------------")

# C. Bucle 'while' para solicitar una entrada hasta que sea correcta
palabra_secreta = "python"
entrada_usuario = ""

print("Adivina la palabra secreta (pista: es un lenguaje de programación).")
while entrada_usuario.lower() != palabra_secreta:
    entrada_usuario = input("Introduce la palabra: ")
    if entrada_usuario.lower() != palabra_secreta:
        print("Incorrecto. ¡Inténtalo de nuevo!")

print("¡Felicidades! Has adivinado la palabra secreta.")


#PASO 3 LISTAS Y DICIONARIOS:
# A. Crear una lista y mostrar cada elemento con un bucle
estudiantes = ["Jhon Rojas", "Evelin Cadena", "Diego Hernández"]
print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(f"- {estudiante}")

print("----------------------------------------------------")

# B. Crear un diccionario y mostrar sus claves y valores
contacto = {
    "nombre": "Evelin Jhoanan Rojas Cadena",
    "correo": "Evelin.rojas@yahoo.com",
    "telefono": "555-1234"
}
print("Información de contacto:")
# El método .items() nos permite recorrer claves y valores al mismo tiempo
for clave, valor in contacto.items():
    print(f"{clave.capitalize()}: {valor}")

print("----------------------------------------------------")

# C. Script para agregar elementos a la lista y actualizar el diccionario
# Agregar un nuevo estudiante a la lista
nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante para agregar a la lista: ")
estudiantes.append(nuevo_estudiante) # .append() agrega un elemento al final de la lista
print("\nLista de estudiantes actualizada:")
for estudiante in estudiantes:
    print(f"- {estudiante}")

# Actualizar un valor en el diccionario
print(f"\nEl teléfono actual de {contacto['nombre']} es {contacto['telefono']}.")
nuevo_telefono = input("Introduce el nuevo número de teléfono: ")
contacto["telefono"] = nuevo_telefono # Se actualiza el valor asociado a la clave "telefono"
print("\nInformación de contacto actualizada:")
for clave, valor in contacto.items():
    print(f"{clave.capitalize()}: {valor}")