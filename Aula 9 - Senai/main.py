# Desafio

# restaurante
# preciso de um cardápio
# # beber - agua - refrigerante - vinho
# comer - macarronada - pizza - camarão
# mostrar as opções que a pessoa escolheu


# Cardápio de restaurante

# # Bebidas
# bebidas = ["água", "refrigerante", "vinho"]

# # Comidas
# comidas = ["macarronada", "pizza", "camarão"]

# # Pedido
# pedido = []

# # Opção de bebida e comida
# for item in bebidas + comidas:
#     escolha = input(f"Deseja pedir {item}? (S/N?: ")
#     if escolha.lower() == "s":
#         pedido.append(item)

# # Resultado
# print("Pedido:")
# for item in pedido:
#     print(item)



# """REGRA UTILIZE A FUNÇÃO EM SUA FORMA PURA"""

#1 CRIE UMA FUNÇÃO PARA SUBTRAIR DOIS NÚMEROS 

#2 CRIE UMA FUNÇÃO PARA SOMAR DOIS NÚMEROS 

#3 CRIE UMA FUNÇÃO PARA DIVIDIR DOIS NÚMEROS 

#4 CRIE UMA FUNÇÃO PARA MULTIPLICAR DOIS NÚMEROS

# DENTRO DA FUNÇÃO PRINCIPAL CHAME TODAS AS OUTRAS:

#5 CRIE UMA CALCULADORA, ONDE O USUÁRIO POSSO ESCOLHER AS OPERAÇÕES 

#DICA - UTILIZE CONDICIONAIS



# Função para subtrair dois números
# def subtrair(a, b):
#     return a - b

# # Função para somar dois números
# def somar(a, b):
#     return a + b

# # Função para dividir dois números
# def dividir(a, b):
#     return a / b if b else "Não é possível dividir por zero."

# # Função para multiplicar dois números
# def multiplicar(a, b):
#     return a * b

# # Função principal da calculadora
# def calculadora():
#     print("Escolha uma operação:")
#     print("1. Subtrair")
#     print("2. Somar")
#     print("3. Dividir")
#     print("4. Multiplicar")
    
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
        
#     escolha = input("Digite o número da operação desejada: ")

#     if escolha == '1':
#         resultado = num1 - num2
#     elif escolha == '2':
#         resultado = num1 + num2
#     elif escolha == '3':
#         resultado = num1 / num2 if num2 != 0 else "Não é possível dividir por zero."
#     elif escolha == '4':
#         resultado = num1 * num2
#     else:
#         print("Escolha inválida. Por favor, digite um número de 1 a 4 para selecionar uma operação.")
#         return

#     print(f"Resultado da operação: {resultado}")

# # Chama a calculadora
# calculadora()