# IMPORTAM MÓDULOS (Adicione estas linhas no topo do arquivo)
from Gato import Gato
from Cachorro import Cachorro
from CachorroDomestico import CachorroDomestico
from Animal import Animal
from Baleia import Baleia

# ANIMAL -> Gato, Cachorro
class Main: # PRINCIPAL -> Somente executa códigos e cria objetos
    print("INICIANDO CLASSE PRINCIPAL")

    gato1 = Gato(idade=2, nome="Tom", regiao="Brasil", cadeiaAlimentar="Carnívoro")
    gato1.comer()
    gato1.dormir()
    gato1.mostrarIdadeDoGato()
    gato1.cospePelo()
    gato1.alimentando()

    cachorro1 = Cachorro(idade=3, nome="Zeus", regiao="Alemanha")
    cachorro1.comer()
    cachorro1.dormir()
    cachorro1.mostrarIdade()
    cachorro1.latir()
    cachorro1.aniversario()

    # CORREÇÃO: Passando os argumentos obrigatórios direto na criação do objeto
    cachorro_domestico = CachorroDomestico(idade=4, nome="Max", regiao="Brasil")
    print(f"O nome do seu cachorro doméstico é: {cachorro_domestico.nome}")

    # Se a sua classe possuir um atributo específico para a raça (como tipo),
    # você pode mantê-lo assim:
    cachorro_domestico.tipo = "Pug"
    print(f"A raça do cachorro é {cachorro_domestico.tipo}")

    # NÃO DEVO INSTANCIAR CLASSE PAI
    girafa = Animal(tipo="Girafa", idade=12, regiao="Japão")
    girafa.comer()
    girafa.dormir()
    girafa.mostrarIdade()

    # CORRETO
    baleia = Baleia("Baleia", 12, "Oceano")
    baleia.comer()
    baleia.dormir()
