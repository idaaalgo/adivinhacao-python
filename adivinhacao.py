print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 16

chute = int(input("Digite seu chute: "))
acertou = chute == numero_secreto
menor = chute < numero_secreto
maior = chute > numero_secreto


if acertou:
    print("Você acertou!!")
else:
    if menor:
        print("Você errou! O seu chute foi menor que o número secreto!!")
    elif maior:
        print("Você errou! O seu chute foi maior que o número secreto!!")

print("Fim de Jogo!!")