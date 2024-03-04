from functions import *

P = np.roll(np.eye(26, dtype=int), 1, axis=0)
E = np.roll(np.eye(26, dtype=int), 2, axis=1)


mensagem = input("Digite a mensagem para ser codificada com cifra simples: ")
print(f"Mensagem Original: {mensagem}")

matriz = para_one_hot(mensagem)
print(matriz)

mensagem = para_string(matriz)
print(f"Mensagem em String: {mensagem}")

mensagem_cifrada = cifrar(mensagem, P)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_original = de_cifrar(mensagem_cifrada, P)
print("Mensagem decifrada:", mensagem_original)


mensagem = input("Digite a mensagem para ser codificada com cifra enigma: ")
print(f"Mensagem Original: {mensagem}")

matriz = para_one_hot(mensagem)
print(matriz)

mensagem = para_string(matriz)
print(f"Mensagem em String: {mensagem}")

mensagem_com_enigma = enigma(mensagem, P, E)
print(f"Mensagem com enigma:", mensagem_com_enigma)

mensagem_original = de_enigma(mensagem_com_enigma, P, E)
print("Mensagem original:", mensagem_original)