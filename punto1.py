import re
letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g':
6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

cadena = "PCLIK OHSGJ CXXDN VITTM ÑAUFM WCGAU WMMYJ UTBLT XDDGV CTXDS RLPFY UOUXZ XLXIG LMVJP OEXZE UDNCN WFCDD GÑUTÑ DQWX"
clave = "ACTITUD"

def descifrado_vigenere(cadena,key):
    letras_invertidas = {v: k for k, v in letras.items()}

    cadena = re.sub(r'[^a-zA-ZñÑ]', '', cadena)
    cadena = cadena.lower()
    key = re.sub(r'[^a-zA-ZñÑ]', '', key)
    key = key.lower()
    text_aux = []
    for i in range(len(cadena)):
        text_aux.append(letras_invertidas[(letras[cadena[i]] -letras[key[i%len(key)]])%27])

    text_aux = "".join(text_aux)
    print(text_aux)

descifrado_vigenere(cadena,clave)