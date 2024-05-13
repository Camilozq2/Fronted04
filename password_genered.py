import random
import string
#generar una contraseña aleatoria de longitud especifica.

# def generate_password(length):
#     characters = string.ascii_letters + string.digits
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password
  
# password_length = 10
# generated_password = generate_password(password_length)
# print(generated_password)

#generar una contraseña aleatoria de longitud especifica con caracteres especiales.

def generar_contraseña(longitud, usar_caracteres_especiales=False):
    caracteres = string.ascii_letters + string.digits
    if usar_caracteres_especiales:
        caracteres += string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def obtener_criterios_contraseña():
    longitud = int(input("Ingrese la longitud deseada de la contraseña: "))
    incluir_caracteres_especiales = input("¿Incluir caracteres especiales? (si/no): ").lower()
    usar_caracteres_especiales = incluir_caracteres_especiales.startswith('s')
    return longitud, usar_caracteres_especiales

def main():
    longitud, usar_caracteres_especiales = obtener_criterios_contraseña()
    contraseña_generada = generar_contraseña(longitud, usar_caracteres_especiales)
    print("Contraseña Generada:", contraseña_generada)

if __name__ == "__main__":
    main()
