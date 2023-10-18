# Exercício 1: Remova o último elemento de uma lista e imprima a lista resultante.

# lista = [1, 2, 3, 4, 5]
# lista.pop(4)
# print(lista)

# Exercício 2: Remova o elemento de índice 2 de uma lista e imprima a lista resultante

# lista = [1, 2, 3, 4, 5]
# lista.pop(1)
# print(lista)

# Exercício 3: Crie uma pilha usando uma lista e implemente as operações  pop().

# Lista inicial
# lista = [1, 2, 3, 4, 5]

# # Adiciona um elemento à pilha usando append()
# lista.append(6)
# print("Elemento 6 adicionado à pilha.")

# # Remove e retorna o elemento do topo da pilha usando pop()
# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()  # Tentativa de remover de uma pilha vazia

# Exercício 4: Remova o primeiro elemento de uma lista e o último elemento usando pop() e imprima a lista resultante.

# lista = [1, 2, 3, 4, 5]
# lista.pop(0)
# lista.pop(-1)
# print(lista)

# Exercício 5: Acesse os três primeiros caracteres de uma string.
# string1 = "Alface"   
# transforma = string1[:3]
# print(transforma)

# Exercício 6: Acesse todos os elementos de uma lista, exceto o primeiro e o último.

# lista = [1, 2, 3, 4, 5]
# acessar_elementos = lista[1:-1]
# print(acessar_elementos)


# Desafio: Calculadora de Média >

# Instruções:

# 1. Peça ao usuário que insira três notas (por exemplo, de 0 a 10).
# 2. Use a função **`input()`** para obter as notas como entrada do usuário e converta-as em números de ponto flutuante.
# 3. Calcule a média das três notas.
# 4. Com base na média, forneça uma avaliação:
#     - Se a média for maior ou igual a 7, imprima "Aprovado".
#     - Se a média for maior ou igual a 5 e menor do que 7, imprima "Recuperação".
#     - Se a média for menor do que 5, imprima "Reprovado".
# 5. Certifique-se de lidar com possíveis erros, como entradas inválidas (por exemplo, notas fora do intervalo de 0 a 10).

# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# n3 = float(input("Digite a terceira nota: "))
# media =(n1 + n2 + n3)/3


# if 0 <= media <= 10:
#     if media >= 7:
#         resultado = "Aprovado"
#     elif media >=5:
#         resultado = "Recuperação"
#     else:
#         resultado = "Reprovado"
#     print(f"Sua média é {media} e você está {resultado}")
# else:
#     print("As notas devem estar entra 0 e 10")



