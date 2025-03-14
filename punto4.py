import math
import re
import numpy

letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g':
6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

#Funcion utilizada para crear la matriz llave
def keyMatrix(Key,n):
    Matrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(letras[Key[i*n+j]])
        Matrix.append(temp)
    if numpy.linalg.det(Matrix)==0:
        print("Clave invalida")
        exit(None)
    return Matrix

#Funcion auxiliar para realizar la multiplicacion de las matrices por capas
def Multiply(X,Y):
    Y=list([letras[x]] for x in Y)
    result=numpy.dot(X,Y)
    return result

#Funcion para crear la matriz cifrada
def Hill_encrypt(Text,KeyMatrix,n):
    letras_invertidas = {v: k for k, v in letras.items()}
    cipher = ''
    for i in range(0,len(Text),n):
        temp=Multiply(KeyMatrix,Text[i:i+n])
        for x in range(n):
            cipher+=letras_invertidas[temp[x][0]%27]
    return cipher


if __name__=="__main__":
    #Se define la entrada de la llave y de el texto
    Key = ''.join(input("Enter the Key: ").lower().split())
    Text = ''.join(input("Enter the Text: ").lower().split())


    #Se saca la raiz a la clave
    #debe tener raiz entera y ser diferente de 0
    n = math.sqrt(len(Key))
    if n != math.trunc(n) or n==0:
        print("Clave invalida")
        exit(None)
    n = int(n)

    #completamos el texto con x para cuando hagamos la matriz
    #poder tener una matriz completa
    if len(Text)%n!=0:
        for i in range(n-len(Text)%n):
            Text+='x'

    #Se crea la matriz llave
    MatrisLlave = keyMatrix(Key,n)

    print()
    print("TExtoCifrado: ",Hill_encrypt(Text,MatrisLlave,n))