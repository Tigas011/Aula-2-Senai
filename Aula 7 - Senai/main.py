# def função_principal():
# #  Bloco de código da função principal
#     variavel1 = 10
#     variavel2 = 20

#     if variavel1 < variavel2:
#     # Bloco de código do if
#          print("Variavel 1 é menor que Variável 2")
#     else:
#     # Bloco de código do else
#          print("Variavel 1 é maior ou igaul a Variável 2")

#     for i in range(5):
#     #  Bloco de código do loop for
#         print(f"Valor de i: {i}")

# Fim do bloco de código da função principal
# Fim do bloco de código do programa principal


# função_principal()

# Estruturas de Repetição

# c = 1
# while c <= 10:
#     print("contador", c)
#     c = c + 3

# Random == aleatorio
# import random
# aleatorio = random.random()
# print(aleatorio)

# # O método randint() da biblioteca random é usado para gerar um número inteiro aleatório dentro de um intervalo especificado.
# x = random.randint(1,500)
# print(x)


import random

print("Jogo de adivinhação, escolha um número e tente adivinhar")

chute = input("Digite um número -> ")

numero_aleatorio = random.randint(1, 2)

chute_int = int(chute)

if chute_int == numero_aleatorio:
    print("Sensacional, vc acertou! O número é", numero_aleatorio)
else:
    print("Não foi dessa vez, vc errou! O número é", numero_aleatorio)


