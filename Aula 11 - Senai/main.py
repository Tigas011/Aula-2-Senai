# def imprimir(n1, n):
#     for i in range(n1,n,2):
#         print(i)


# imprimir(2,10)

# def soma_lista(lista):
#     soma = 0
#     for numero in lista:
#         soma += numero
#     return soma

# soma_lista([1, 2, 3])

# Exercício 1: Escreva uma função que calcule a soma dos números de 1 a N, onde N é um número inteiro dado. 

# def soma_de_1_a_n(n):
#     return (n * (n + 1)) / 2

# print(soma_de_1_a_n(5))

# Exercício 2: Escreva uma função que conte quantas vezes uma letra específica aparece em uma palavra.

# def conta_letra(palavra, letra):
#     contador = 0
#     for caractere in palavra:
#         if caractere == letra:
#             contador += 1
#     return contador

# print(conta_letra("banana", "a"))

# # Exercício 3: Escreva uma função que calcule o fatorial de um número inteiro não negativo N.

# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# print(fatorial(4))

# Exercício 4: Crie um Dicionário, adicione elementos ao dicionário e os mostre na tela.

# dicionario = dict()

# dicionario["nome"] = "Tigas"
# dicionario["idade"] = 20
# dicionario["curso"] = "Programação em Python"

# print(dicionario)

# Exercício 5: Utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

# Crie um dicionário para armazenar os produtos e seus preços
produtos = {}

# Peça para o usuário inserir o nome e o preço de três produtos
# for i in range(3):
#     produto = input("Nome do produto: ")
#     preco = float(input("Preço do produto: "))
#     produtos[produto] = preco

# # Mostre os produtos e seus preços na tela
# for produto, preco in produtos.items():
#     print("Nome do produto:", produto)
#     print("Preço do produto:", preco)