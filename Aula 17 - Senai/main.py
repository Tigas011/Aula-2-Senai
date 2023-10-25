# class Casa:  #Classe sendo criada
#     def __init__(self, color, height):
#         self.color = color                          #ATRIBUTOS
#         self.height = height                        #ATRIBUTOS
#     #metodo
#     def display(self):
#         print(self.color, self.height)

# casa = Casa('blue', 100) #objeto sendo instanciado
# print(casa.display())


# class Retangulo:   #Classe sendo criada
#     def __init__(self, largura, altura):
#         self.altura = altura                      #ATRIBUTOS
#         self.largura = largura                    #ATRIBUTOS

#     #METODO
#     def area(self):
#         return self.largura * self.altura
    
#     def soma_area(self):
#         return self.largura + self.altura


# retangulo0 = Retangulo(5, 10)
# retangulo1 = Retangulo(10, 30)
# retangulo2 = Retangulo(10, 3)



# print(retangulo1.area(), retangulo0.soma_area())
# print(retangulo2.area(), retangulo2.soma_area())

# class Cadastro:
#     def __init__(self, email, name, age):
#         self.email = email
#         self.age = age
#         self.name = name

#     def display(self):
#         self.email = input("Digite aqui o seu email: ")
#         self.name = input("Digite aqui o seu nome: ")
#         self.age = input("Digite aqui a sua idade: ")

#     def get_email(self):
#         return self.email

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

# cadastro = Cadastro('juio@gmail.com', 'Julio', 18)
# cadastro.display()

# print("Email:", cadastro.get_email())
# print("Nome:", cadastro.get_name())
# print("Idade:", cadastro.get_age())


# 1 - Crie uma classe chamada Cachorro com um atributo nome e um método 
# latir que imprima "Woof!" quando chamado. 
# Em seguida, crie um objeto da 
# classe Cachorro e chame o método latir.

# class Cachorro:
#     def __init__(self, nome):
#         self.nome = nome

#     def latir(self):
#         print("Woof!")

# cachorro1 = Cachorro("Rex")
# cachorro1.latir()






# 2Crie uma classe chamada Retangulo com atributos largura e 
# altura. Adicione um método chamado calcular_area que retorna a área do retângulo.
# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcular_area(self):
#         return self.largura * self.altura

# retangulo1 = Retangulo(5, 3)
# area = retangulo1.calcular_area()
# print("Área do retângulo:", area)





# 3: Crie uma classe chamada Carro com um atributo chamado velocidade 
# (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta a
# velocidade em 5 unidades a cada vez que é chamado.

# class Carro:
#     def __init__(self):
#         self.velocidade = 0

#     def acelerar(self):
#         self.velocidade += 5

# carro1 = Carro()
# print("Velocidade inicial do carro:", carro1.velocidade)
# carro1.acelerar()
# print("Velocidade após acelerar:", carro1.velocidade)





# 4 - Crie uma classe chamada Gato que herda da classe Cachorro do exercício anterior. 
#  O método latir da classe Cachorro deve ser substituído por um método miar na classe 
# Gato que imprime "Miau!".

# class Gato(Cachorro):
#     def miar(self):
#         print("Miau!")

# gato1 = Gato("Frajola")
# gato1.miar()



# Exercício 4: Crie uma classe chamada ContaBancaria com um atributo saldo inicializado com 0. Em seguida, crie métodos deposito e saque que atualizem o saldo. Crie um objeto da classe ContaBancaria, faça um depósito e um saque, e imprima o saldo resultante.

class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def deposito (self, valor):
        self.saldo += valor

    def saque (self, valor):
        self.saldo -= valor

conta = ContaBancaria()
conta.deposito(float(input("Insira o valor do depósito: ")))
conta.saque(float(input("Inisira o valor desejado para saque: ")))
print(f"O saldo da sua conta bancária é de, {conta.saldo} reais.")
