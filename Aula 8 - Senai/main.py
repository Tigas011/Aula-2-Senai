# Ele importa a biblioteca random (assumindo que ela foi importada anteriormente no código).

# Ele gera três números inteiros aleatórios e os armazena nas variáveis n1, n2 e n3, cada um dentro do intervalo de 5 a 10 (inclusive).

# Ele imprime os valores de n1, n2 e n3 em linhas separadas.

# Em seguida, ele gera um único número inteiro aleatório e o armazena na variável n1, desta vez dentro do intervalo de 10 a 29 (inclusive).

# Por fim, ele imprime o valor da variável n1 atualizada.



# import random

# n1 = random.randint(5,10)
# n2 = random.randint(5,10)
# n3 = random.randint(5,10)
# print (n1,"\n",n2,"\n",n3)

# n1 = random.randrange(10,30)
# print(n1)



# Entendi que você tem uma tupla chamada numeros_add com seis elementos, e você está acessando o elemento na posição 3 (índice 3) dessa tupla e armazenando-o na variável ultima_tupla. Em seguida, você está imprimindo o valor armazenado em ultima_tupla. No seu exemplo, o valor na posição 3 da tupla numeros_add é 89, e esse valor será impresso na saída. Portanto, o resultado deste código será imprimir "89" na tela.
# numeros_add = (1, 3, 645, 89, 79, 45)
# ultima_tupla = numeros_add[3]
# print(ultima_tupla)

#Metodo lista

# tupla1 = (1,2,24,432,43)
# print(tupla1)
# #Neste momento estou transformando a tupla em lista
# transform = list(tupla1)
# print (transform)

# letras = ['a', 'e', 'i', 'o', 'u']

# for vogal in letras:
#     print(vogal)



#empacotar em python
# Você possui uma tupla chamada regiao com dois elementos: "Cataratas" e "Amazonia".

# Usando a linha s, n = regiao, você está desempacotando os elementos da tupla regiao nas variáveis s e n. Isso significa que "Cataratas" será atribuído à variável s e "Amazonia" será atribuído à variável n.

# Em seguida, você imprime o valor de s com a mensagem "Regiao Sul" usando print("Regiao Sul", s), e depois imprime o valor de n da mesma forma, mas com a mensagem "Regiao Sul" usando print("Regiao Sul", n).
# regiao = ("Cataratas","Amazonia")
# s,n = regiao
# print("Regiao Sul",s)
# print("Regiao Sul",n)



# Crie uma tupla chamada frutas com pelo menos 5 frutas diferentes. Em seguida, acesse e imprima o terceiro elemento da tupla.  
# frutas = ("uva", "maça", "abacaxi", "banana", "kwui", "morango")
# print(frutas[2])

# Crie uma tupla chamada numeros com alguns números inteiros. Em seguida, converta essa tupla em uma lista e imprima a lista resultante.
# numeros = (1, 3, 6, 512, 78)
# numeros_lista = list(numeros)
# print(numeros_lista)

# Crie uma tupla chamada `meses` com os nomes dos meses do ano até Setembro. Use um loop `for` para imprimir cada mês em uma linha separada.
# meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro")

# for mes in meses:
#     print(mes)


#Crie uma lista chamada notas com algumas notas de alunos. Em seguida, converta essa lista em uma tupla e imprima a tupla resultante.
# notas = [2, 3, 6, 78, 9, 12]
# notas_tupla = tuple(notas)
# print(notas_tupla)


#Crie uma lista chamada ponto que represente as coordenadas (x, y) de um ponto. Em seguida, desempacote os elementos da lista em duas variáveis separadas (x e y) e imprima os valores.
# ponto = (25, 16, 78)
# x, y, i = ponto

# print("Coordenada x:", x)
# print("Coordenada y:", y)
# print("Coordenada i:", i)

# def soma():
#   a = 15
#   b = 10
#   print (a+b)
# soma()


# def cumprimento ():
#   print("Olá boa Tarde")
# cumprimento()


# a = 10
# if a >1:
#   cumprimento()
#   soma()







# def cumprimento(nome, idade):
#     print(f'Olá, {nome}! Você tem {idade} anos de idade.')

# def subtracao():
#     a = int(input("Digite um número: "))
#     b = int(input("Digite outro número: "))
#     resultado = a - b
#     print(f'A subtração de {a} e {b} é igual a {resultado}')

# nome_usuario = input("Digite o seu nome: ")
# idade_usuario = input("Digite a sua idade: ")
# cumprimento(nome_usuario, idade_usuario)

# subtracao()

# def soma(a, b):
#     return a + b

# def subtracao(a, b):
#     return a - b

# def multiplicacao(a, b):
#     return a * b

# def divisao(a, b):
#     if b == 0:
#         return "Erro: Divisão por zero!"
#     else:
#         return a / b

# def calculadora(a, b):
#     print("A Soma desses números é ->", soma(a, b))
#     print("A Subtração desses números é ->", subtracao(a, b))
#     print("A Multiplicação desses números é ->", multiplicacao(a, b))
#     print("A Divisão desses números é ->", divisao(a, b))

# calculadora(10, 3)


# Função principal da calculadora
# def calculadora():
#     print("Selecione uma operação:")
#     print("1. Somar")
#     print("2. Subtrair")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Verificar igualdade")
    
#     escolha = input("Digite o número da operação desejada: ")
    
#     if escolha in ('1', '2', '3', '4', '5'):
#         num1 = float(input("Digite o primeiro número: "))
#         num2 = float(input("Digite o segundo número: "))
        
#         if escolha == '1':
#             resultado = num1 + num2
#         elif escolha == '2':
#             resultado = num1 - num2
#         elif escolha == '3':
#             resultado = num1 * num2
#         elif escolha == '4':
#             if num2 == 0:
#                 resultado = "Erro: Divisão por zero"
#             else:
#                 resultado = num1 / num2
#         else:
#             resultado = num1 == num2
        
#         print(f"Resultado: {resultado}")
#     else:
#         print("Opção inválida")

# Chamando a função principal da calculadora
#


def calculadora():

    print("Selecione uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Verificar igualdade")
    
    escolha = input("Digite o número da operação desejada: ")
    
    if escolha in ('1', '2', '3', '4', '5'):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        if escolha == '1':
            resultado = num1 + num2
        elif escolha == '2':
            resultado = num1 - num2
        elif escolha == '3':
            resultado = num1 * num2
        elif escolha == '4':
            if num2 == 0:
                resultado = "Erro: Divisão por zero"
            else:
                resultado = num1 / num2
        else:
            resultado = num1 == num2
        
        print(f"Resultado: {resultado}")
    else:
        print("Opção inválida")
calculadora ()
escolha = input("Digite o número da operação desejada: ")
calculadora()
