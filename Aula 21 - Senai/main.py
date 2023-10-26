# TRY E EXCEPT

# O uso dos blocos `try` e `except` em Python é fundamental para lidar com exceções, ou seja, 
# situações inesperadas ou erros que podem ocorrer durante a execução de um programa. Aqui está uma explicação mais detalhada desses blocos:

# Bloco `try`:

# - O bloco `try` é usado para envolver um código que pode gerar exceções.
# - Ele define uma seção protegida do código onde você espera que exceções possam ocorrer.
# - Se uma exceção ocorrer dentro do bloco `try`, o Python interromperá a execução normal do programa e procurará por um bloco `except` correspondente para lidar com a exceção.

# Bloco `except`:

# - O bloco `except` é usado para tratar exceções específicas que podem ocorrer dentro do bloco `try`.
# - Você pode ter um ou mais blocos `except` após um bloco `try`, cada um lidando com um tipo específico de exceção.
# - Quando uma exceção ocorre dentro do bloco `try`, o Python verifica os blocos `except` para encontrar um que corresponda ao tipo de exceção.
# - O bloco `except` correspondente é executado, permitindo que você lide com a exceção de acordo com suas necessidades. 
# Você pode exibir uma mensagem de erro, registrar informações ou executar qualquer outra ação apropriada.

# try:
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite outro número: "))
#     resultado = num1 / num2
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")
# except ValueError:
#     print("Erro: Digite números válidos.")
# else:
#     print("O resultado é:", resultado)

# Neste exemplo:

# - O bloco `try` envolve o código que tenta converter entradas do usuário em números inteiros e realizar uma divisão.
# - Se ocorrer uma exceção de divisão por zero (`ZeroDivisionError`) ou uma exceção de valor inválido (`ValueError`), os blocos `except` correspondentes lidarão com essas exceções.
# - O bloco `else` é executado se nenhuma exceção ocorrer no bloco `try`, permitindo que você execute código adicional após a conclusão bem-sucedida do bloco `try`.

# Em resumo, o bloco `try` e o bloco `except` são usados para controlar o tratamento de exceções em Python, 
# permitindo que você lide com erros de forma adequada e evite que o programa seja interrompido abruptamente.


#ALGUNS ERROS FAMOSOS:

# | TypeError | Surge quando uma função ou operação é aplicada a um objeto de tipo incorreto |

# | UnboundLocalError | Surge quando uma referência é feita para uma variável local em uma função ou método, porém nenhum valor está preso à variável |

# | UnicodeError | Surge quando existe um erro relacionado a Unicode codificação ou decodificação |

# | UnicodeEncodeError | Surge quando um erro de codificação de Unicode ocorre |

# | UnicodeDecodeError | Surge quando um erro de decodificação de Unicode ocorre |

# | UnicodeTranslateError | Surge quando um erro de tradução de Unicode ocorre |

# | ValueError | Surge quando uma função pega um argumento de tipo correto, porém de valor impróprio |

# | ZeroDivisionError | Surge quando a segunda divisão ou módulo é zero |

# a = 0
# b = 10
# try:
#     print(a,b)

# except NameError:
#     print("erro de digitação, não existe variável")
# else:
#     print(a, 'oi')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# EXERCÍCIOS:

# Exercício 1: Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# def ler_numero():
#     try:
#         return int(input("Digite um número inteiro: "))
#     except ValueError:
#         print("O valor inserido não é um número inteiro.")


# numero = ler_numero()
# print(f"O número inserido é: {numero}")

# Exercício 2: Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação.

# def dividir(numero_1, numero_2):
#     try:
#         return numero_1 / numero_2
#     except ZeroDivisionError:
#         print("Não é possível dividir por zero.")


# numero_1 = float(input("Digite o primeiro número: "))
# numero_2 = float(input("Digite o segundo número: "))

# resultado = dividir(numero_1, numero_2)
# print(f"O resultado da divisão é: {resultado}")

# Exercício 3: Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido.

# def acessar_lista(lista, indice):
#     if len(lista) <= indice:
#         return None
#     return lista[indice]


# lista = ["a", "b", "c"]
# indice = 2

# elemento = acessar_lista(lista, indice)
# print(f"O elemento na posição {indice} é: {elemento}")


# Exercício 4: Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

# def dividir(numero_1, numero_2):
#     try:
#         return numero_1 / numero_2
#     except ZeroDivisionError:
#         return None


# numero_1 = float(input("Digite o primeiro número: "))
# numero_2 = float(input("Digite o segundo número: "))

# resultado = dividir(numero_1, numero_2)
# print(f"O resultado da divisão é: {resultado}")
