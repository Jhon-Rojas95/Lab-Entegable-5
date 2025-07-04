# Actividad 1. Uso de Python básico.
# 1. Escribir un programa que imprima un mensaje en la consola.
print("¡Bienvenido al Laboratorio entregable No5 de Fundamentos de Python!")
print("For Jhon Steven Rojas Cadena")
print("----------------------------------------------------")

# 2. Declarar variables de diferentes tipos y realizar operaciones matemáticas.
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

# 3. Concatenar cadenas de texto y utilizar funciones básicas como print() y input().
# Concatenación
nombre_usuario = input("Por favor, introduce tu nombre: ")
mensaje_bienvenida = saludo + ", " + nombre_usuario + "!"
print(mensaje_bienvenida)

# Uso de f-strings (una forma más moderna y legible de formatear cadenas)
edad_usuario_str = input("¿Cuántos años tienes? ")
# La función input() siempre devuelve una cadena (str), hay que convertirla si queremos usarla como número.
edad_usuario_int = int(edad_usuario_str) 

print(f"¡Genial, {nombre_usuario}! Entonces tienes {edad_usuario_int} años.")