# Questão 1: Sistema de Gestão de Zoológico


class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = 0
        self.idade = idade
        self.__nivel_fome = 0
        self.nivel_fome = nivel_fome

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = valor

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, valor):
        if valor < 0:
            self.__nivel_fome = 0
        elif valor > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = valor

    def alimentar(self, porcao):
        if porcao <= 0:
            print("Erro: Porção inválida")
        else:
            self.nivel_fome -= porcao

    def emitir_som(self):
        print(f"{self.nome} faz um som genérico.")

    def exibir_resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Nível de fome: {self.nivel_fome}")


class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh

    def correr(self):
        self.nivel_fome += 20
        print(f"{self.nome} correu a {self.__velocidade_kmh} km/h!")

    def emitir_som(self):
        print(f"{self.nome} ruge alto!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade de corrida: {self.__velocidade_kmh} km/h")


class Ave(Animal):
    def __init__(self, nome, idade, nivel_fome, envergadura_asas):
        super().__init__(nome, idade, nivel_fome)
        self.__envergadura_asas = envergadura_asas

    def voar(self):
        if self.nivel_fome > 80:
            print(f"Voo negado: {self.nome} está faminto demais para voar!")
        else:
            print(
                f"{self.nome} voou com suas asas de "
                f"{self.__envergadura_asas}cm!"
            )
            self.nivel_fome += 15

    def emitir_som(self):
        print(f"{self.nome} canta um som melodioso!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das asas: {self.__envergadura_asas} cm")


# Instanciando os animais.
leao = Mamifero(nome="Simba", idade=5, nivel_fome=70, velocidade_kmh=80)
gaviao = Ave(nome="Sky", idade=2, nivel_fome=75, envergadura_asas=120)

# Tentativas de alteração direta dos atributos privados.
leao.__nivel_fome = -999
leao.__idade = -10

# Testando ações que alteram o estado interno via herança e encapsulamento.
leao.correr()
gaviao.voar()
gaviao.voar()

# Testando alimentação.
leao.alimentar(50)
leao.alimentar(-10)

# Exibição final dos resumos.
print("\n--- RESUMO DO MAMÍFERO ---")
leao.emitir_som()
leao.exibir_resumo()

print("\n--- RESUMO DA AVE ---")
gaviao.emitir_som()
gaviao.exibir_resumo()
