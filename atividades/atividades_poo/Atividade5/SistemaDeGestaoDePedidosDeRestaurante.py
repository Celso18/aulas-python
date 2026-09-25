class ItemPedido:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        try:
            # Trata casos em que o valor vem como string com vírgula (ex: '5,50')
            if isinstance(valor, str):
                valor_limpo = valor.replace(',', '.')
            else:
                valor_limpo = valor
            self.valor = float(valor_limpo)
        except (ValueError, TypeError):
            raise ValueError(f"O valor para {self.descricao} deve ser estritamente numérico.")


class Mesa:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []  # Lista interna para armazenar instâncias de ItemPedido (Composição)

    def adicionar_pedido(self, item):
        self.pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}.")

    def somar_total(self):
        return sum(item.valor for item in self.pedidos)

    def fechar_conta(self, taxa_servico):
        subtotal = self.somar_total()
        valor_taxa = subtotal * (taxa_servico / 100)
        total_final = subtotal + valor_taxa

        print(f"\n=== EXTRATO: {self.numero_mesa} ===")
        if not self.pedidos:
            print("Nenhum pedido registrado nesta mesa.")
        else:
            for item in self.pedidos:
                print(f"- {item.descricao}: R$ {item.valor:.2f}")

        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Taxa de serviço ({taxa_servico}%): R$ {valor_taxa:.2f}")
        print(f"Total final: R$ {total_final:.2f}")
        print("================================")

        # Esvazia a lista liberando a mesa
        self.pedidos = []


# Função auxiliar para simular a interface do sistema e capturar as exceções sem quebrar o app
def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)
    except ValueError as erro:
        print(f"ALERTA DO SISTEMA: {erro}")


# 1. Instanciando as mesas
mesa1 = Mesa("Mesa 1")

# 2. Registrando pedidos válidos
registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)

# 3. Testando o Tratamento de Exceções (Simulando erro de digitação do garçom)
print("\n--- TESTANDO ENTRADA INVÁLIDA ---")
registrar_pedido_seguro(mesa1, "Pudim", "quinze")  # Deve exibir o ALERTA DO SISTEMA e não quebrar
registrar_pedido_seguro(mesa1, "Café", "5,50")  # Tratado com sucesso via replace de vírgula

# 4. Adicionando mais um pedido válido após o erro
registrar_pedido_seguro(mesa1, "Suco de Laranja", 12.00)

# 5. Fechando a conta com 10% de taxa de serviço
print("\n--- FECHAMENTO DA CONTA ---")
mesa1.fechar_conta(taxa_servico=10)

# 6. Verificando se a mesa foi limpa
print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")
mesa1.fechar_conta(taxa_servico=10)  # A conta deve vir zerada
