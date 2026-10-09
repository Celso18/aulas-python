from abc import ABC, abstractmethod



# 1. CLASSE PAI ABSTRATA

class Notificador(ABC):
    """
    Classe abstrata que serve como contrato para todos os sistemas de notificação.
    """

    # Método Concreto (Comum a todas as classes filhas)
    def registrar_log(self, destino: str) -> None:
        print(f"[LOG CENTRAL] Iniciando processo de envio para: {destino}")

    # Método Abstrato (Contrato obrigatório)
    @abstractmethod
    def enviar(self, destino: str, mensagem: str) -> None:
        pass



# 2. CLASSES FILHAS (IMPLEMENTAÇÃO)

class NotificacaoSMS(Notificador):
    """
    Classe filha para envio de SMS. Requer validação do número de telefone.
    """

    def enviar(self, destino: str, mensagem: str) -> None:
        # Validação: Remove espaços e verifica se tem apenas números e pelo menos 9 dígitos
        apenas_numeros = "".join(caractere for caractere in destino if caractere.isdigit())

        if len(apenas_numeros) >= 9:
            print(f"[SMS] Enviado com sucesso para {destino}: \"{mensagem}\"")
        else:
            print(f"[ERRO SMS] Falha ao enviar. O número '{destino}' deve conter pelo menos 9 dígitos.")


class NotificacaoEmail(Notificador):
    """
    Classe filha para envio de E-mail. Requer validação básica do caractere '@'.
    """

    def enviar(self, destino: str, mensagem: str) -> None:
        # Validação: Verifica se o e-mail possui uma estrutura mínima com '@'
        if "@" in destino and "." in destino:
            print(f"[E-MAIL] Mensagem enviada para <{destino}>: \"{mensagem}\"")
        else:
            print(f"[ERRO E-MAIL] Falha ao enviar. O endereço '{destino}' é inválido.")



# 3. SISTEMA (FUNÇÃO POLIMÓRFICA EXTERNA)

def processar_lote(lista_de_objetos: list, destino_padrao: str, mensagem_padrao: str) -> None:
    """
    Função externa que demonstra o Polimorfismo.
    O sistema confia no contrato estabelecido pela classe abstrata.
    """
    print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
    for item in lista_de_objetos:
        # Chama o método concreto herdado da classe pai
        item.registrar_log(destino_padrao)

        # Chama o método que era abstrato, mas que está implementado na filha
        item.enviar(destino_padrao, mensagem_padrao)
        print("-" * 40)



# 4. ROTEIRO DE TESTES OBRIGATÓRIOS


# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente as linhas abaixo para testar e provar que o Python bloqueia:
# try:
#     objeto_generico = Notificador()
# except TypeError as e:
#     print(f"\n[TESTE ERRO] Bloqueio de instância abstrata funcionou! Erro: {e}")

# 2. Instanciando as Classes Filhas
sms_valido = NotificacaoSMS()
email_valido = NotificacaoEmail()

# 3. Criando um Lote de Processamento (Lista)
lote = [sms_valido, email_valido, sms_valido]  # Repetindo tipos conforme o roteiro

# 4. Processando em lote com dados válidos
processar_lote(lote, destino_padrao="11999998888", mensagem_padrao="Seu código de acesso é 4321.")

# --- Teste Extra: Demonstrando as validações individuais de negócio ---
print("\n--- TESTE EXTRA: VALIDAÇÕES DE NEGÓCIO ---")
sms_invalido = NotificacaoSMS()
email_invalido = NotificacaoEmail()

sms_invalido.registrar_log("1234")
sms_invalido.enviar("1234", "Oi")

print("-" * 40)

email_invalido.registrar_log("usuario_sem_arroba.com")
email_invalido.enviar("usuario_sem_arroba.com", "Bem-vindo!")
