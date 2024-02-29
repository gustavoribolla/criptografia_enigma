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
    
    return msg_matriz

# print(para_one_hot("abc"))

def para_string(M): #RIBAS
    return 

def cifrar(msg, P): #RAFA
    msg_matriz = para_one_hot(msg)
    msg_cifrada = np.dot(P, msg_matriz)

    return msg_cifrada



def de_cifrar(msg, P): #RIBAS
    return 

def enigma(msg, P, E): #RAFA
    msg_matriz = para_one_hot(msg)

    msg_cifrada = msg_matriz

    for j in range(len(msg_matriz[0])):
        n_msg = np.dot(P, msg_cifrada)
        for i in range (len(msg_matriz)):
            msg_cifrada[i][j] = n_msg[i][j]
        P = np.dot(P, E)


    return msg_cifrada

cifra = np.roll(np.eye(26, dtype=int), 1, axis=1)
e = np.roll(np.eye(26, dtype=int), 2, axis=1)




def de_enigma(msg, P, E): #RIBAS
    return