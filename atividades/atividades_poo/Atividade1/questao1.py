# --- CLASSE CARRO ---
class Carro:
    # 1 Construtor e seus 5 Atributos
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False  # Todo carro inicia desligado

    # Método Convencional 1: Ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} ligou: Vrummm!")
        else:
            print(f"{self.modelo} já está ligado.")

    # Método Convencional 2: Desligar o carro
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.modelo} foi desligado.")
        else:
            print(f"{self.modelo} já está desligado.")

    # Método Convencional 3: Retornar ficha técnica rápida
    def obter_ficha_tecnica(self) -> str:
        return f"{self.marca} {self.modelo} ({self.ano}) - Cor: {self.cor}"


# --- EXECUÇÃO FORA DA CLASSE ---

# Instanciação de 5 objetos diferentes
carro1 = Carro("Toyota", "Corolla", 2023, "Prata")
carro2 = Carro("Ford", "Mustang", 2022, "Preto")
carro3 = Carro("Chevrolet", "Onix", 2024, "Branco")
carro4 = Carro("Volkswagen", "Golf", 2020, "Vermelho")
carro5 = Carro("Honda", "Civic", 2021, "Cinza")

# Testando um método rápido antes de listar
carro2.ligar()

# Armazenando os objetos em uma lista fora da classe
lista_de_carros = [carro1, carro2, carro3, carro4, carro5]

# Exibindo a lista de objetos
print("\n--- LISTA DE CARROS INSTANCIADOS ---")
for carro in lista_de_carros:
    print(carro.obter_ficha_tecnica())
