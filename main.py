from core.auth import criar_conta, login
from core.bank import ver_saldo, depositar, sacar, historico
from core.utils import carregar, salvar

def menu(user, dados):
    while True:
        print(f"\n=== Conta: {user} ===")
        print("1 - Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Histórico")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == "1":
            ver_saldo(dados, user)

        elif op == "2":
            depositar(dados, user)
            salvar(dados)

        elif op == "3":
            sacar(dados, user)
            salvar(dados)

        elif op == "4":
            historico(dados, user)

        elif op == "5":
            break

def main():
    dados = carregar()

    while True:
        print("\n=== NeoBank CLI ===")
        print("1 - Criar conta")
        print("2 - Login")
        print("3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            criar_conta(dados)
            salvar(dados)

        elif op == "2":
            user = login(dados)
            if user:
                menu(user, dados)

        elif op == "3":
            break

if __name__ == "__main__":
    main()