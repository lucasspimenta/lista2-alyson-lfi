import random

def escolher_palavra():
    palavras = ["python", "programacao", "jogo", "computador", "desenvolvimento"]
    return random.choice(palavras)

def inicializar_palavra_secreta(palavra):
    return "_" * len(palavra)

def exibir_palavra_secreta(palavra_secreta):
    print("Palavra Secreta: " + " ".join(palavra_secreta))

def atualizar_palavra_secreta(palavra, palavra_secreta, letra):
    nova_palavra_secreta = list(palavra_secreta)
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra_secreta[i] = letra
    return "".join(nova_palavra_secreta)

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    return resposta.lower() == "s"

def jogo_da_forca():
    vidas_maximas = 10
    vidas_restantes = vidas_maximas
    palavra = escolher_palavra()
    palavra_secreta = inicializar_palavra_secreta(palavra)

    while True:
        print("\n" + "=" * 30)
        exibir_palavra_secreta(palavra_secreta)
        print("Vidas Restantes: ", vidas_restantes)

        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            palavra_secreta = atualizar_palavra_secreta(palavra, palavra_secreta, letra)
            if palavra_secreta == palavra:
                print("\nParabéns! Você venceu!")
                break
        else:
            vidas_restantes -= 1
            if vidas_restantes == 0:
                print("\nVocê perdeu! A palavra secreta era: " + palavra)
                break

    if jogar_novamente():
        jogo_da_forca()

jogo_da_forca()
