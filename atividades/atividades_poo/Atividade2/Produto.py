# Questão 1: Sistema de Controle de Estoque


class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade <= 0:
            print("Erro: Quantidade inválida")
        elif quantidade > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            self.__quantidade_estoque -= quantidade
            print("Venda realizada com sucesso")

    def aplicar_desconto(self, percentual):
        if 0 < percentual <= 80:
            self.__preco *= 1 - percentual / 100
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Quantidade em estoque: {self.__quantidade_estoque}")


meu_produto = Produto("Notebook", 3500.00, 10)

# Tentativas de alteração direta: criam atributos externos e não alteram os privados.
meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100

# Tentativa de venda maior que o estoque real.
meu_produto.realizar_venda(9999)

# O resumo confirma que os dados privados continuam protegidos.
meu_produto.exibir_resumo()

