import numpy as np


def para_one_hot(msg): #RAFA
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_matriz = np.eye(26, dtype=int)
    

    indices = []
    msg_matriz = []

    for i in range(len(msg)):
        for j in range(len(alfabeto)):
            if msg[i] == alfabeto[j]:
                indices.append(j)
   
    for indice in indices:
        coluna = []
        for linha in alfabeto_matriz:
            coluna.append(linha[indice])
        msg_matriz.append(coluna)

    
 

    msg_matriz = np.array(msg_matriz)
    msg_matriz = msg_matriz.transpose()
    # msg_codificada = np.dot(msg_matriz, cifra)
    
    return msg_matriz


def para_string(M): #RIBAS
    return 

def cifrar(msg, P): #RAFA
    msg_matriz = para_one_hot(msg)
    msg_cifrada = np.dot(P, msg_matriz)

    return msg_cifrada

cifra = np.roll(np.eye(26, dtype=int), 1, axis=0)
print(cifra)
print(cifrar("baabc", cifra))

def de_cifrar(msg, P): #RIBAS
    return 

def enigma(msg, P, E): #RAFA
    return 

def de_enigma(msg, P, E): #RIBAS
    return