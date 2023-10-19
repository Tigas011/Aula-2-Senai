# Módulos em Python são arquivos que contêm um conjunto de funções, 
# variáveis e classes que você pode usar em seus programas Python. 
# Eles permitem organizar e reutilizar código, tornando seus programas 
# mais eficientes e mais fáceis de manter. qui estão alguns módulos Python:

# 1. math:
#    O módulo math fornece funções matemáticas, como operações de aritmética, 
# trigonometria, exponenciação, raiz quadrada, etc.

#    Exemplo de uso:

#    import math
#    print(math.sqrt(25))  # Calcula a raiz quadrada de 25


# 2. random:
#    O módulo random permite gerar números aleatórios e é útil para jogos, 
# simulações e outras aplicações que envolvem aleatoriedade.

#    Exemplo de uso:
   
#    import random
#    print(random.randint(1, 6))  # Gera um número aleatório entre 1 e 6
 

# 3. os:
#    O módulo os fornece funções para interagir com o sistema operacional, 
# permitindo que você manipule diretórios, arquivos e execute comandos do sistema.

#    Exemplo de uso:
   
#    import os
#    print(os.getcwd())  # Obtém o diretório de trabalho atual


# 4. datetime:
#    O módulo datetime oferece classes e funções para trabalhar com datas e horas.

#    Exemplo de uso:

#    from datetime import datetime
#    data_atual = datetime.now()
#    print(data_atual)


# 5. json:
#    O módulo json é usado para trabalhar com dados JSON, que são comuns 
# em comunicação de dados na web.

#    Exemplo de uso:

#    import json
#    dados = '{"nome": "João", "idade": 30}'
#    objeto = json.loads(dados)
#    print(objeto["nome"])

# Python possui uma vasta biblioteca padrão com muitos outros módulos que 
podem ser explorados à medida que você ganha experiência com a linguagem. Além disso, 
você também pode criar seus próprios módulos para organizar seu código em 
projetos maiores.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Exercício 1: Calcule a raiz quadrada de um número inteiro inserido pelo usuário usando o módulo math
  
# import math

# # Solicita um número inteiro ao usuário
# n = int(input("Digite um número inteiro: "))

# # Calcula a raiz quadrada do número
# raiz = math.sqrt(n)

# # Imprime o resultado
# print("A raiz quadrada de {} é {}.".format(n, raiz))

# Exercício 2: Calcule o valor absoluto de um número decimal inserido pelo usuário usando o módulo math

# import math

# # Solicita um número decimal ao usuário
# x = float(input("Digite um número decimal: "))

# # Calcula o valor absoluto do número
# abs = math.fabs(x)

# # Imprime o resultado
# print("O valor absoluto de {} é {}.".format(x, abs))

# Exercício 3: Arredonde um número decimal inserido pelo usuário para o inteiro mais próximo usando o módulo math

# import math

# # Solicita um número decimal ao usuário
# x = float(input("Digite um número decimal: "))

# # Arredonda o número para o inteiro mais próximo
# arredondamento = math.floor(x + 0.5)

# # Imprime o resultado
# print("O arredondamento de {} é {}.".format(x, arredondamento))

# Exercício 4: Calcule o seno de um ângulo em graus inserido pelo usuário usando o módulo math.

# import math

# # Solicita um ângulo em graus ao usuário
# angulo = float(input("Digite um ângulo em graus: "))

# # Calcula o seno do ângulo
# seno = math.sin(math.radians(angulo))

# # Imprime o resultado
# print("O seno de {} graus é {}.".format(angulo, seno))






