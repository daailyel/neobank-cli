from getpass import getpass

def criar_conta(dados):
    user = input("Usuário: ")

    if user in dados:
        print("❌ Usuário já existe!")
        return

    senha = getpass("Senha: ")

    dados[user] = {
        "senha": senha,
        "saldo": 0.0,
        "historico": []
    }

    print("✅ Conta criada!")

def login(dados):
    user = input("Usuário: ")
    senha = getpass("Senha: ")

    if user in dados and dados[user]["senha"] == senha:
        print("🔓 Login feito!")
        return user
    else:
        print("❌ Erro no login")
        return None