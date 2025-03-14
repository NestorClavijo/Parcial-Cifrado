class AlfabetoVernam():
  diccionarioVernam = {
    '0': '000000', '1': '000001', '2': '000010', '3': '000011', '4': '000100', '5': '000101', '6': '000110', '7': '000111',
    '8': '001000', '9': '001001', 'A': '001010', 'B': '001011', 'C': '001100', 'D': '001101', 'E': '001110', 'F': '001111',
    'G': '010000', 'H': '010001', 'I': '010010', 'J': '010011', 'K': '010100', 'L': '010101', 'M': '010110', 'N': '010111',
    'Ñ': '011000', 'O': '011001', 'P': '011010', 'Q': '011011', 'R': '011100', 'S': '011101', 'T': '011110', 'U': '011111',
    'V': '100000', 'W': '100001', 'X': '100010', 'Y': '100011', 'Z': '100100', 'a': '100101', 'b': '100110', 'c': '100111',
    'd': '101000', 'e': '101001', 'f': '101010', 'g': '101011', 'h': '101100', 'i': '101101', 'j': '101110', 'k': '101111',
    'l': '110000', 'm': '110001', 'n': '110010', 'ñ': '110011', 'o': '110100', 'p': '110101', 'q': '110110', 'r': '110111',
    's': '111000', 't': '111001', 'u': '111010', 'v': '111011', 'w': '111100', 'x': '111101', 'y': '111110', 'z': '111111'
  }

  def getValue(self,key):
    return self.diccionarioVernam[key]

  def getKey(self, value):
    for key, diccValue in self.diccionarioVernam.items():
      if value == diccValue:
        return key

def cifradorVernam(cadenaATratar, clave):
  alfabetoVernam = AlfabetoVernam()
  cadenaATratar = cadenaATratar.replace(" ", "")
  clave = clave.replace(" ", "")
  cadenaTratada = ""

  if len(clave) < len(cadenaATratar):
    print("Clave invalida")
    return

  for i in range(0, len(cadenaATratar)):
    aux = ''
    #Bucle para iterar por cada bit del diccionario de vernam
    for j in range(0,6):
      bitCadena = alfabetoVernam.getValue(cadenaATratar[i])[j] #Auxiliar para acceder a cada bit de la cadena
      bitClave = alfabetoVernam.getValue(clave[i])[j] #Auxiliar para acceder a cada bit de la clave K
      if bitCadena != bitClave: #Función XOR en Strings
        aux += '1'
      else:
        aux += '0'
    cadenaTratada += alfabetoVernam.getKey(aux)

  return cadenaTratada

C = "NESTORJAVIERCLAVIJOHERNANDEZ"
K = "MlG5ST4M2J1T9C00PRxBwCH6RD7S"
print(cifradorVernam(C, K))