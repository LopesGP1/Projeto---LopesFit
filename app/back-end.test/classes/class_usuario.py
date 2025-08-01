
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao_bd.conexaoBD import conectar_banco
from funcao_data import data_hoje
from mensagens import mensagens_validadoras
from validators import valid_email

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.__email = email # protegido (encapsulado)
        self.__senha = senha # protegido (encapsulado)
        
    # Getter para email
    def get_email(self):
        return self.__email
    # Setter para email
    def set_email(self, novo_email):
        if "@" in novo_email and "." in novo_email:
            self.__email = novo_email
        else:
            print("Email inválido.")    
     # Getter para senha (opcional, cuidado com segurança)
    def get_senha(self):
        return "******"  # nunca exibir a senha real
    # Setter para senha
    def set_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            print("Senha muito curta.")
            
    def cadastrar_usuario(self,nome,email,senha,data_cadastro):
        try:
            conexao = conectar_banco()
            if not conexao:
                return mensagens_validadoras.Mensagens.erro_conexao_bd("Erro ao conectar ao banco de dados.")
            
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO tb_usuario (nome,email,senha,data_cadastro) VALUES (%s, %s, %s,%s)",
            (nome, email, senha, data_cadastro)
            )
            conexao.commit() 
            return mensagens_validadoras.Mensagens.Mensagens_sucesso("Usuário cadastrado com sucesso!")
        except Exception as erro:
            return mensagens_validadoras.Mensagens.Mensagens_erro("Ocorreu um erro ao cadastrar o usuário:", erro)
        finally:
             # Sempre fecha a conexão se ela foi aberta
            if 'conexao' in locals() and conexao:
                conexao.close()
            

    
    def editar_nome_completo(self, novo_nome, email):
        try:
            conexao = conectar_banco()
            if not conexao:
                return mensagens_validadoras.Mensagens.erro_conexao_bd("Erro ao conectar ao banco de dados.")

            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE tb_usuario SET nome = %s WHERE email = %s",
                (novo_nome, email)
            )
            conexao.commit()
            return mensagens_validadoras.Mensagens.Mensagens_sucesso("Nome atualizado com sucesso!")
        except Exception as erro:
            return mensagens_validadoras.Mensagens.Mensagens_erro(f"Erro ao atualizar o nome: {erro}")
        finally:
            if 'conexao' in locals() and conexao:
                conexao.close()
    def editar_Senha(self, nova_senha, email):
        try:
            if len(nova_senha) < 6:
                return mensagens_validadoras.Mensagens.Mensagens_validacoes("A nova senha deve ter pelo menos 6 caracteres.")
            
            conexao = conectar_banco()
            if not conexao:
                return mensagens_validadoras.Mensagens.erro_conexao_bd("Erro ao conectar ao banco de dados.")

            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE tb_usuario SET senha = %s WHERE email = %s",
                (nova_senha, email)
            )
            conexao.commit()
            return mensagens_validadoras.Mensagens.Mensagens_sucesso("Senha atualizada com sucesso!")
        except Exception as erro:
            return mensagens_validadoras.Mensagens.Mensagens_erro(f"Erro ao atualizar a senha: {erro}")
        finally:
            if 'conexao' in locals() and conexao:
                conexao.close()
    def editar_email(self, novo_email, email_atual):
        try:
            if "@" not in novo_email or "." not in novo_email:
                return mensagens_validadoras.Mensagens.Mensagens_validacoes("O novo email é inválido.")

            conexao = conectar_banco()
            if not conexao:
                return mensagens_validadoras.Mensagens.erro_conexao_bd("Erro ao conectar ao banco de dados.")
            
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE tb_usuario SET email = %s WHERE email = %s",
                (novo_email, email_atual)
            )
            conexao.commit()
            return mensagens_validadoras.Mensagens.Mensagens_sucesso("Email atualizado com sucesso!")
        except Exception as erro:
            return mensagens_validadoras.Mensagens.Mensagens_erro(f"Erro ao atualizar o email: {erro}")
        finally:
            if 'conexao' in locals() and conexao:
                conexao.close()
    def excluir_conta(self, email):
        try:
            conexao = conectar_banco()
            if not conexao:
                return mensagens_validadoras.Mensagens.erro_conexao_bd("Erro ao conectar ao banco de dados.")

            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM tb_usuario WHERE email = %s",
                (email,)
            )
            conexao.commit()
            return mensagens_validadoras.Mensagens.Mensagens_sucesso("Conta excluída com sucesso!")
        except Exception as erro:
            return mensagens_validadoras.Mensagens.Mensagens_erro(f"Erro ao excluir conta: {erro}")
        finally:
            if 'conexao' in locals() and conexao:
                conexao.close()
    @staticmethod
    def teste_defs_usuario():
        usuario = None  # variável para armazenar o usuário atual

        while True:
            print('='*30)
            print("\n--- INICIANDO TESTES DA CLASSE USUÁRIO ---")
            print('='*30)
            print("1. Cadastrar usuário")
            print("2. Editar nome")
            print("3. Editar senha")
            print("4. Editar email")
            print("5. Excluir conta")
            print("6. Mostrar dados / Testar setters")
            print("0. Sair")
            opcao = input("Digite a opção para teste: ")

            if opcao == "1":
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                while not valid_email.verificar_email_valido(email):
                    print("❌ Email inválido.")
                    email = input("Digite o email novamente: ")
                senha = input("Digite a senha: ")
                data = data_hoje()

                usuario = Usuario(nome, email, senha)
                print(usuario.cadastrar_usuario(nome, email, senha, data))

            elif opcao == "2":
                if usuario:
                    novo_nome = input("Digite o novo nome: ")
                    print(usuario.editar_nome_completo(novo_nome, usuario.get_email()))
                else:
                    print("⚠️ Nenhum usuário cadastrado.")

            elif opcao == "3":
                if usuario:
                    nova_senha = input("Digite a nova senha: ")
                    print(usuario.editar_Senha(nova_senha, usuario.get_email()))
                else:
                    print("⚠️ Nenhum usuário cadastrado.")

            elif opcao == "4":
                if usuario:
                    novo_email = input("Digite o novo email: ")
                    while not valid_email.verificar_email_valido(novo_email):
                        print("❌ Email inválido.")
                        novo_email = input("Digite o novo email novamente: ")
                    print(usuario.editar_email(novo_email, usuario.get_email()))
                else:
                    print("⚠️ Nenhum usuário cadastrado.")

            elif opcao == "5":
                if usuario:
                    print(usuario.excluir_conta(usuario.get_email()))
                    usuario = None  # remove o usuário atual da sessão
                else:
                    print("⚠️ Nenhum usuário cadastrado.")

            elif opcao == "6":
                if usuario:
                    print("Email (getter):", usuario.get_email())
                    print("Senha (getter):", usuario.get_senha())

                    usuario.set_email("novoemail@example.com")
                    print("Novo email (válido):", usuario.get_email())

                    usuario.set_senha("novasenha123")
                    print("Nova senha (válida):", usuario.get_senha())

                    usuario.set_email("emailinvalido")  # inválido
                    usuario.set_senha("123")  # inválido
                else:
                    print("⚠️ Nenhum usuário cadastrado.")

            elif opcao == "0":
                print("--- TESTES FINALIZADOS ---\n")
                break

            else:
                print("❌ Opção inválida.")
        
if __name__ == "__main__":
    opcao = input("Deseja testar o sistema no terminal? (s/n): ").lower()
    if opcao == "s":
        Usuario.teste_defs_usuario()
    
    