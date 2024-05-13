import random

def validar_numero(func):
    def wrapper(*args, **kwargs):
        numero = func(*args, **kwargs)
        if 1 <= numero <= 100:
            return numero
        else:
            print("El número debe estar entre 1 y 100.")
    return wrapper

@validar_numero
def obtener_numero():
    return int(input("Ingresa un número entre 1 y 100: "))

def adivina_el_numero():
    print("Bienvenido a Adivina el Número")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intentos += 1
        intento = obtener_numero()
        
        if not intento:
            continue
        
        if intento < numero_secreto:
            print("El número es más grande. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es más pequeño. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

def la_computadora_adivina():
    print("Piensa en un número entre 1 y 100, y yo intentaré adivinarlo.")
    input("Presiona Enter cuando estés listo ")
    
    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intento = random.randint(limite_inferior, limite_superior)
        print(f"¿Es {intento} tu número?")
        respuesta = input("Indica si es demasiado bajo (b), demasiado alto (a) o correcto (c): ").lower()
        
        if respuesta == 'c':
            print(f"¡Excelente! Adiviné tu número en {intentos} intentos.")
            break
        elif respuesta == 'b':
            limite_inferior = intento + 1
        elif respuesta == 'a':
            limite_superior = intento - 1
        
        intentos += 1

if __name__ == "__main__":
    print("Bienvenido a Juegos de Adivina el Número")
    opcion = input("Selecciona una opción:\n1. Adivina el número\n2. La computadora adivina\n")
    
    if opcion == '1':
        adivina_el_numero()
    elif opcion == '2':
        la_computadora_adivina()
    else:
        print("Opción no válida. Por favor selecciona 1 o 2.")
