class Animal:
    def __init__(self, nome: str, idade: int, nivel_fome: int):
        self.__nome = nome
        self.__idade = 0  # Inicializa para passar pela validação do setter
        self.idade = idade
        self.__nivel_fome = 0  # Inicializa para passar pela validação do setter
        self.nivel_fome = nivel_fome

    # Getter e Setter para Nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    # Getter e Setter para Idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = nova_idade

    # Getter e Setter para Nível de Fome
    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, nova_fome):
        if nova_fome < 0:
            self.__nivel_fome = 0
        elif nova_fome > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = nova_fome

    # Métodos de comportamento
    def alimentar(self, porcao):
        if porcao <= 0:
            print("Erro: Porção inválida")
        else:
            self.nivel_fome -= porcao  # O próprio setter garante o limite mínimo de 0

    def emitir_som(self):
        print(f"{self.nome} faz um som genérico.")

    def exibir_resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Nível de Fome: {self.nivel_fome}/100")


class Mamifero(Animal):
    def __init__(self, nome: str, idade: int, nivel_fome: int, velocidade_kmh: float):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh

    @property
    def velocidade_kmh(self):
        return self.__velocidade_kmh

    @velocidade_kmh.setter
    def velocidade_kmh(self, nova_velocidade):
        self.__velocidade_kmh = nova_velocidade

    def correr(self):
        print(f"{self.nome} correu a {self.velocidade_kmh} km/h!")
        self.nivel_fome += 20  # Utiliza a propriedade (setter) herdada do pai

    def emitir_som(self):
        print(f"{self.nome} ruge/ruge alto!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade de Corrida: {self.velocidade_kmh} km/h")


class Ave(Animal):
    def __init__(self, nome: str, idade: int, nivel_fome: int, envergadura_asas: int):
        super().__init__(nome, idade, nivel_fome)
        self.__envergadura_asas = envergadura_asas

    @property
    def envergadura_asas(self):
        return self.__envergadura_asas

    @envergadura_asas.setter
    def envergadura_asas(self, nova_envergadura):
        self.__envergadura_asas = nova_envergadura

    def voar(self):
        if self.nivel_fome > 80:
            print(f"Voo negado: {self.nome} está faminto demais para voar!")
        else:
            print(f"{self.nome} voou com suas asas de {self.envergadura_asas}cm!")
            self.nivel_fome += 15  # Utiliza a propriedade (setter) herdada do pai

    def emitir_som(self):
        print(f"{self.nome} canta um som melodioso!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das Asas: {self.envergadura_asas} cm")


# ==============================================================================
# TESTES OBRIGATÓRIOS DA ATIVIDADE
# ==============================================================================

# Instanciando os animais
leao = Mamifero(nome="Simba", idade=5, nivel_fome=70, velocidade_kmh=80)
gaviao = Ave(nome="Sky", idade=2, nivel_fome=75, envergadura_asas=120)

# 1. Tentativa de alteração direta dos atributos privados (Proteção do Encapsulamento)
# No Python, as tentativas abaixo criam novos atributos dinâmicos locais na instância,
# mas não corrompem os atributos reais protegidos (__nivel_fome e __idade do escopo da classe)
leao.__nivel_fome = -999
leao.__idade = -10

# 2. Testando ações que alteram o estado interno via Herança e Encapsulamento
leao.correr()         # Fome sobe de 70 para 90
gaviao.voar()         # Fome sobe de 75 para 90 (Sucesso)
gaviao.voar()         # Fome está em 90 -> Deve exibir: "Voo negado: Sky está faminto demais para voar!"

# 3. Testando alimentação
leao.alimentar(50)    # Fome cai de 90 para 40
leao.alimentar(-10)   # Deve exibir: "Erro: Porção inválida"

# 4. Exibição final dos resumos
print("\n--- RESUMO DO MAMÍFERO ---")
leao.emitir_som()
leao.exibir_resumo()

print("\n--- RESUMO DA AVE ---")
gaviao.emitir_som()
gaviao.exibir_resumo()
