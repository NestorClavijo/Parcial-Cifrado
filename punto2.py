#@title Descifrar afin sin conocer el valor de a y b(prueba todas las posibles combinaciones)
import sympy

# Alfabeto con 27 caracteres (incluyendo la Ñ)
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Función para calcular el inverso modular de 'a'
def inverso_modular(a, m):
    try:
        return sympy.mod_inverse(a, m)
    except ValueError:
        return None  # No hay inverso modular

# Función para descifrar un texto cifrado con el mtodo afín
def descifrar_afin(texto_cifrado, a, b, alfabeto):
    a_inv = inverso_modular(a, len(alfabeto))  # Calcular inverso modular de a
    if a_inv is None:
        return None  # No se puede descifrar si 'a' no tiene inverso
    m_descifrado = ""

    for letra in texto_cifrado:
        if letra in alfabeto:
            C_val = alfabeto.index(letra)
            M_val = (a_inv * (C_val - b)) % len(alfabeto)
            m_descifrado += alfabeto[M_val]
        else:
            m_descifrado += letra

    return m_descifrado

def generar_alfabeto_descifrado(a, b, alfabeto):
    a_inv = inverso_modular(a, len(alfabeto))
    if a_inv is None:
        return None

    nuevo_alfabeto = [""] * len(alfabeto)
    for i in range(len(alfabeto)):
        C_val = (a * i + b) % len(alfabeto)
        nuevo_alfabeto[C_val] = alfabeto[i]

    return "".join(nuevo_alfabeto)


encrypted_text = input("Ingrese el texto cifrado: ").upper().replace(" ", "")  # Convertir a mayúsculas y eliminar espacios


print("\nProbando todas las combinaciones de a y b...\n")
for a in range(1, 27):
    if inverso_modular(a, 27) is None:
        continue
    for b in range(27):
        mensaje_descifrado = descifrar_afin(encrypted_text, a, b, alfabeto)
        if mensaje_descifrado:
            nuevo_alfabeto = generar_alfabeto_descifrado(a, b, alfabeto)
            print(f"\n>>> Clave encontrada: a = {a}, b = {b}")
            print(f"Mensaje descifrado: {mensaje_descifrado}")
            print(f"Nuevo alfabeto generado: {nuevo_alfabeto}\n")