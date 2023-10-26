# Exercício 1:
# Crie uma classe chamada Animal com um método falar() 
# que exibe "Som de animal desconhecido". Em seguida, crie uma classe 
# Cachorro que herda de Animal e substitui o 
# método falar() para exibir 
# "Rugir". Crie uma instância de onça e 
# chame o método falar().

class Animal:

    def falar(self):
        print("Som de animal desconhecido")


class Cachorro(Animal):

    def falar(self):
        print("Rugir")


if __name__ == "__main__":
    cachorro = Cachorro()
    cachorro.falar()










# Exercício 2:
# Crie uma classe chamada Veiculo com um atributo 
# velocidade 
# inicializado com 0. Em seguida, crie uma classe 
# Nave que herda de
#  Veiculo e possui um método acelerar() que aumenta 
# a velocidade em 
# 10 unidades. Crie uma instância de Carro, chame 
# acelerar() três vezes 
# e exiba a velocidade final.


class Veiculo:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def get_velocidade(self):
        return self.velocidade

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade


class Nave(Veiculo):

    def acelerar(self):
        self.velocidade += 10


if __name__ == "__main__":
    nave = Nave()
    nave.acelerar()
    nave.acelerar()
    nave.acelerar()
    print(nave.get_velocidade())




# Exercício 3:
# Crie uma classe Pessoa com atributos nome e idade. 
# Em seguida, crie uma classe Estudante que 
# herda de Pessoa 
# e adiciona um atributo matricula. Crie uma 
# instância de Estudante 
# e exiba o nome, idade e matrícula.

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade


class Estudante(Pessoa):

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula


if __name__ == "__main__":
    estudante = Estudante("Fulano", 20, 123456)
    print(estudante.get_nome())
    print(estudante.get_idade())
    print(estudante.get_matricula())
