# nome = "Otavio Mesquita"
# comprimento = len(nome)
# print(comprimento)

# x = "Guarulhos"
# tipo = type(x)
# print(tipo)

# x = input("Digite um numero, um texto... vc q sabe")
# tipo = type(x)
# print(tipo)

# n = "8"
# x = int(n)
# print(x+8)

# n1 = 250
# c = str(n1)
# print(c,"Pessoas aqui? Oloko em")

# texto = "Hello"
# lista = list(texto)
# print(lista)

#Tuplas são daos que não podem ser alterados "Constantes"
# tupla = (20,5,6,18)
# tupla = (403,520,221)
# print(tupla)

# list = [14,56,2]
# list2 = tuple(list)
# print(list2)

# Range
# numeros = range(1,11)
# for i in numeros:
#     print(i)

# numeros = [3,1,4,1,5,9,2,6,5,3,5]
# minimo = min(numeros)
# maximo = max(numeros)
# print("O número máximo é:", maximo, "e o minimo é:", minimo)

# list1 = ["b", "d", "e","f"]
# list2 = sorted*(list)
# print(list)

# Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

# numeros = range(2,21,2)
# for i in numeros:
#      print(i)

# Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 de 5 a 50 e, em seguida, calcule e imprima a soma desses múltiplos.

# numeros = range(5,51,5)
# for i in numeros:
#      print(i)

# Exercício 3: Escreva um programa que use a função type() para verificar o tipo de uma variável.

# x = bool(input("Digite um numero "))
# tipo = type(x)
# print(tipo)

# Exercício 4: Escreva um programa que use a função print() para imprimir uma mensagem de saudação personalizada, incluindo o nome do usuário.

# nome = input("Qual é o seu nome? ")
# print("Olá, {}! Seja bem-vindo(a) ao meu programa. Espero que voDcê se divirta.".format(nome))

# 5 Exercício 5: Escreva um programa que use a função range() para gerar os números ímpares de 1 a 10 e, em seguida, calcule e imprima a média desses números.

numeros = list(range(1, 11))
media = sum(numeros) / len(numeros)
print(media)

