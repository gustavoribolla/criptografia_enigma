from codificador_de_matrizes_rafaela_ribolla import *

P = np.roll(np.eye(26, dtype=int), 1, axis=0)
E = np.roll(np.eye(26, dtype=int), 2, axis=1)

rodar = True

while rodar:

    tipo = input("Digite 1 para cifra simples, 2 para cifra enigma, 4 para decifrar simples, 5 para decifrar engima, 6 para sair: ")

    if tipo == "1":

        mensagem = input("Digite a mensagem para ser codificada com cifra simples: ")
        print(f"Mensagem Original: {mensagem}")

        matriz, validacao = para_one_hot(mensagem)
        print(matriz)

        if validacao:
            mensagem = para_string(matriz)
            print(f"Mensagem em String: {mensagem}")

            mensagem_cifrada = cifrar(mensagem, P)
            print("Mensagem cifrada:", mensagem_cifrada)


    if tipo == "2":

        mensagem = input("Digite a mensagem para ser codificada com cifra enigma: ")
        print(f"Mensagem Original: {mensagem}")

        matriz, validacao = para_one_hot(mensagem)
        print(matriz)

        if validacao:
            mensagem = para_string(matriz)
            print(f"Mensagem em String: {mensagem}")

            mensagem_com_enigma = enigma(mensagem, P, E)
            print(f"Mensagem com enigma:", mensagem_com_enigma)


    if tipo == "4":
        mensagem = input("Digite a mensagem para ser decodificada com cifra simples: ")
        print(f"Mensagem Original: {mensagem}")

        matriz, validacao = para_one_hot(mensagem)
        print(matriz)

        if validacao:
            mensagem_original = de_cifrar(mensagem, P)
            print("Mensagem decifrada:", mensagem_original)

    if tipo == "5":
        mensagem = input("Digite a mensagem para ser decodificada com cifra enigma: ")
        print(f"Mensagem Original: {mensagem}")

        matriz, validacao = para_one_hot(mensagem)
        print(matriz)

        if validacao:
            mensagem_original = de_enigma(mensagem, P, E)
            print("Mensagem decifrada:", mensagem_original)

    if tipo == "6":
        rodar = False
        print("Saindo do programa")