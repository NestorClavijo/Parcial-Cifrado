def construir_matriz(clave):

    clave = clave.upper()
    clave_filtrada = [letra for letra in clave if letra not in "ÑW"]

    alfabeto = "ABCDEFGHIJ" + "KLMNOPQRSTUV" + "XYZ"

    # se añaden los datos de la clave
    matriz_lista = []
    for letra in clave_filtrada:
        if letra in alfabeto and letra not in matriz_lista:
            matriz_lista.append(letra)

    # se completa el alfabeto
    for letra in alfabeto:
        if letra not in matriz_lista:
            matriz_lista.append(letra)

    # la lista se transforma en un matriz de 5x5
    return [matriz_lista[i:i + 5] for i in range(0, 25, 5)]


def buscar_posicion(matriz, letra):
    for fila_idx, fila in enumerate(matriz):
        if letra in fila:
            return fila_idx, fila.index(letra)
    return None


def descifrar_playfair(cifrado, clave):
    matriz = construir_matriz(clave)

    # Eliminar espacios
    mensaje_procesado = "".join(cifrado.upper().split())
    resultado = ""

    for pos in range(0, len(mensaje_procesado), 2):
        par = mensaje_procesado[pos:pos + 2]
        if len(par) < 2:
            break

        pos1 = buscar_posicion(matriz, par[0])
        pos2 = buscar_posicion(matriz, par[1])
        if pos1 is None or pos2 is None:
            print(f"Error: No se encontró la posición para el par '{par}'")
            return None

        r1, c1 = pos1
        r2, c2 = pos2

        if r1 == r2:
            resultado += matriz[r1][(c1 - 1) % 5] + matriz[r2][(c2 - 1) % 5]
        elif c1 == c2:
            resultado += matriz[(r1 - 1) % 5][c1] + matriz[(r2 - 1) % 5][c2]
        else:
            resultado += matriz[r2][c1] + matriz[r1][c2]

    return resultado


clave = "SEGURIDAD"
texto_cifrado = "OBSGVHGSOBQG USOIGCGEIXGEQPSEBYRG ISJQJDBCFCDABASKVHOIDVI XCHHRD JLBGSE GHDUD CGOBSGVHGSQANPUNEMGCDVQ JMUQGKCNSGIHD UQXACGI OIDP OHDPEOIODGSJADVGSJCMDHDUNVHSDVMDHDRBGQZBSGSRHEOBGGH"

mensaje = descifrar_playfair(texto_cifrado, clave)
print("Mensaje descifrado:")
print(mensaje)