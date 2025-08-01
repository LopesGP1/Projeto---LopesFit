class Mensagens:
    @staticmethod
    def Mensagens_sucesso(msg):
        return f"[SUCESSO] {msg}"

    @staticmethod
    def Mensagens_erro(msg, erro=None):
        return f"[ERRO] {msg} {erro if erro else ''}"

    @staticmethod
    def Mensagens_validacoes(msg):
        return f"[VALIDAÇÃO] {msg}"

    @staticmethod
    def erro_conexao_bd(msg):
        return f"[ERRO CONEXÃO] {msg}"
