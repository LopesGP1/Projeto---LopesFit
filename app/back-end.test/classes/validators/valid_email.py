import re

def verificar_email_valido(email):
    # Expressão regular básica para validar e-mails
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(padrao_email, email):
        return True
    else:
        return False

# Testando o script
if __name__ == "__main__":
    email_teste = input("Digite um e-mail para verificar: ")

    if verificar_email_valido(email_teste):
        print("✅ E-mail válido!")
    else:
        print("❌ E-mail inválido.")
