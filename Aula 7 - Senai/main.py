def função_principal():
# #  Bloco de código da função principal
    variavel1 = 10
    variavel2 = 20

    if variavel1 < variavel2:
    # Bloco de código do if
         print("Variavel 1 é menor que Variável 2")
    else:
    # Bloco de código do else
         print("Variavel 1 é maior ou igaul a Variável 2")

    for i in range(5):
    #  Bloco de código do loop for
        print(f"Valor de i: {i}")

# Fim do bloco de código da função principal
# Fim do bloco de código do programa principal


função_principal()

# Estruturas de Repetição

c = 1
while c <= 10:
    print("contador", c)
    c = c + 3

Random == aleatorio
import random
aleatorio = random.random()
print(aleatorio)

# O método randint() da biblioteca random é usado para gerar um número inteiro aleatório dentro de um intervalo especificado.
x = random.randint(1,500)
print(x)


 import random

def adivinha_numero():
    numero_aleatorio = random.randint(12, 25)

    for tentativas in range(3):
        chute = input("Digite um numero entre 12 e 25: ")

        if chute == numero_aleatorio:
            print("Você acertou!")
            return

        else:
            print("Seu chute foi alto ou baixo.")

    print("Você perdeu!")

if __name__ == "__main__":
    adivinha_numero()

# import random

# # Gera um número flutuante com ponto flutuante
# numero_aleatorio = random.random()
# print (numero_aleatorio)
# # GEra um número aleatório inteiro
# numero_aleatorio2 = random.randint(10,25)
# print (numero_aleatorio2)
 
# import random

# def adivinha_numero():
#     numero_aleatorio = random.randint(12, 25)

#     for tentativas in range(3):
#         chute = input("Digite um numero entre 12 e 25: ")

#         if chute == numero_aleatorio:
#             print("Você acertou!")
#             return

#         else:
#             print("Seu chute foi alto ou baixo.")

#     print("Você perdeu!")

# if __name__ == "__main__":
#     adivinha_numero()

# Exercício 1: Contagem regressiva simples. Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".

# contador = 10
# while contador >= 1:
#     print(contador)
#     contador -= 1

# print("Fogo!")

# contador é inicializado com o valor 10.
# A condição do loop while é verificada. Enquanto contador for maior ou igual a 1, o código dentro do loop será executado.
# Dentro do loop, print(contador) exibe o valor atual de contador.
# Em seguida, contador é decrementado em 1 com contador -= 1. Isso significa que o valor de contador é reduzido em 1 a cada iteração do loop.
# O loop continua a ser executado até que a condição contador >= 1 não seja mais verdadeira. Isso acontece quando contador atinge o valor 0, porque 0 não é maior ou igual a 1.
# Portanto, o resultado desse código será a contagem regressiva de 10 até 1, com cada número sendo impresso em uma linha separada. Quando o loop terminar, o valor de contador será 0, e a execução do programa continuará após o loop.


# Exercício 2: Soma de números pares. Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

# numero = int(input("Digite um número inteiro positivo: "))
# soma = 0
# for i in range(2, numero + 1):
#     if i % 2 == 0:
#         soma += i
#         print("A soma dos números pares de 2 até {} é {}".format(numero, soma))

#  Solicita ao usuário que insira um número inteiro positivo.
# Verifica se o número inserido é positivo (maior ou igual a zero). Se o número for negativo, exibe uma mensagem dizendo que o número inserido não é positivo.
# Se o número inserido for positivo, ele inicializa uma variável chamada soma com o valor 0. Esta variável será usada para calcular a soma dos números pares.
# Em seguida, utiliza um loop for para iterar através dos números pares a partir de 2 até o número inserido (incluindo o próprio número, se ele for par). O terceiro argumento em range(2, numero + 1, 2) é 2, que especifica o passo da iteração, ou seja, ele pega todos os números pares dentro do intervalo.
# Durante cada iteração do loop, o número atual (par) é adicionado à variável soma.
# Finalmente, exibe a soma dos números pares de 2 até o número inserido.
# Este código calculará corretamente a soma dos números pares dentro do intervalo especificado e informará ao usuário o resultado. Se o número inserido não for positivo, ele informará que o número não é positivo. Caso contrário, calculará a soma dos números pares no intervalo.



# Exercício 3: Tabuada de multiplicação. Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.

# for i in range(1, 11):
#     for j in range(1, 11):
#         resultado = i * j
#         print(f"{i} x {j} = {resultado}")
         
# O primeiro loop for é usado para iterar de 1 a 10, representado pela variável i. Este loop controla a multiplicação principal.
# O segundo loop for é aninhado dentro do primeiro e também itera de 1 a 10, representado pela variável j. Este loop controla os múltiplos de i para gerar as equações de multiplicação.
# Dentro dos loops, a variável resultado é calculada como o produto de i e j, ou seja, resultado = i * j.
# Em seguida, é usada a função print para exibir a equação de multiplicação e seu resultado formatado como uma string. Por exemplo, se i for 2 e j for 3, o programa imprimirá "2 x 3 = 6".
# Os loops aninhados continuarão a executar até que todas as combinações de multiplicação de 1 a 10 tenham sido impressas.
# O resultado final será a tabuada de multiplicação completa do 1 ao 10, com todas as equações e resultados impressos na saída.

