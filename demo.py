from functions import *

mensagem = "spfc"
P = np.roll(np.eye(26, dtype=int), 1, axis=0)
mensagem_cifrada = cifrar(mensagem, P)
print("Mensagem cifrada:", mensagem_cifrada)

P = np.roll(np.eye(26, dtype=int), 1, axis=0)
mensagem_original = de_cifrar(mensagem_cifrada, P)
print("Mensagem decifrada:", mensagem_original)

cifra = np.roll(np.eye(26, dtype=int), 1, axis=1)
e = np.roll(np.eye(26, dtype=int), 2, axis=1)