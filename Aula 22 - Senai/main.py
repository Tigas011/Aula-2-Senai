# WITH EM PYTHON

# A palavra-chave `with` em Python é usada para criar um contexto controlado para um bloco de código. 
# É frequentemente usado com objetos que precisam ser gerenciados, como arquivos, conexões de banco de dados ou recursos do sistema que precisam ser abertos e fechados adequadamente. 
# A principal vantagem do uso de `with` é que ele garante que os recursos sejam liberados automaticamente quando não são mais necessários, mesmo se ocorrerem exceções no bloco de código.

# A sintaxe básica do `with` é a seguinte:

# with contexto as variavel:
     # Código dentro do contexto

# O objeto "contexto" deve ser um objeto que suporta o protocolo do gerenciador de contexto, ou seja, ele deve ter métodos `__enter__()` e `__exit__()` definidos.

# Aqui está um exemplo prático do uso de `with` com arquivos:

# Abrir um arquivo e ler seu conteúdo
# with open('exemplo.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# O arquivo é automaticamente fechado após sair do bloco "with"

# Neste exemplo, o `with` é usado com `open()` para abrir um arquivo chamado "exemplo.txt" no modo de leitura ('r'). 
# O arquivo é automaticamente fechado quando saímos do bloco `with`, garantindo que os recursos do sistema sejam liberados corretamente.

# Você também pode criar seus próprios gerenciadores de contexto definindo classes com os métodos `__enter__()` e `__exit__()` para personalizar o comportamento do contexto. 
# Isso pode ser útil em situações em que você precisa de um controle mais preciso sobre o que acontece antes e depois do contexto.

# Exemplos de código com with

# import os

# Criar um diretório usando "with"
# with open('novo_diretorio', 'w') as novo_diretorio:
#     os.mkdir('novo_diretorio')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# with open('exemplo.txt', 'r') as arquivo:
#     conteúdo = arquivo.read()
#     print(conteúdo)

# Abrindo um arquivo

# MANIPULANDO O DIRETÓRIO

# Exemplo 1: Criar um Diretório


# import os
# with os.scandir('c:/Users/aluno/Desktop/aula12/t') as entrada:
#       for arquivo in entrada:
#          print(f'Diretório encontrado: {arquivo.name}')


# Exemplo 2: Entrar em um Diretório

# import os
#  with os.scandir('c:/Users/aluno/Desktop/aula12') as entrada:
#     for arquivo in entrada:
#          if arquivo.is_file():
#              print(f'Arquivo encontrado: {arquivo.name}')



# Exemplo 3: Renomear um Diretório

# import os
# os.rename('exemplo.txt', 'test5.txt')



# Exemplo 4: Remover um Diretório

# import shutil
# shutil.rmtree('c:/Users/aluno/Desktop/aula12/')



# Exemplo 5: Listar Arquivos em um Diretório

# import os
# with os.scandir('meu_diretorio') as entrada:
#     for arquivo in entrada:
#         if arquivo.is_file():
#             print(f'Arquivo encontrado: {arquivo.name}')



# Exemplo 6: Copiar Arquivos de um Diretório para Outro

# import shutil
# os.rename('exemplo.txt', 'test5.txt')



# Esses exemplos são mais concisos e realizam operações comuns de manipulação de diretórios usando a estrutura with. 
# Certifique-se de o código seja executado em um ambiente em que você tenha as permissões necessárias para as operações de sistema de arquivos.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# EXERCÍCIOS:

# Exercício 1: Criar um Diretório

# import os

# # Criar um diretório
# os.mkdir("novo_diretorio")

# # Verificar se o diretório foi criado
# if os.path.exists("novo_diretorio"):
#     print("O diretório foi criado com sucesso.")
# else:
#     print("O diretório não foi criado.")


# Exemplo 2: Entrar em um Diretório

# import os

# # Criar um diretório
# os.mkdir("novo_diretorio")

# # Entrar no diretório
# os.chdir("novo_diretorio")

# # Verificar se o diretório atual foi alterado
# if os.getcwd() == "novo_diretorio":
#     print("O diretório atual foi alterado com sucesso.")
# else:
#     print("O diretório atual não foi alterado.")


