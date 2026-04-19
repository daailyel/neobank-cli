from datetime import datetime

def registrar(dados, user, msg):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    dados[user]["historico"].append(f"[{data}] {msg}")

def ver_saldo(dados, user):
    print(f"💰 Saldo: R${dados[user]['saldo']:.2f}")

def depositar(dados, user):
    try:
        valor = float(input("Valor: "))
        if valor <= 0:
            print("❌ Valor inválido")
            return

        dados[user]["saldo"] += valor
        registrar(dados, user, f"Depósito R${valor:.2f}")
        print("✅ Depósito feito")

    except:
        print("❌ Erro")

def sacar(dados, user):
    try:
        valor = float(input("Valor: "))
        if valor <= 0 or valor > dados[user]["saldo"]:
            print("❌ Saque inválido")
            return

        dados[user]["saldo"] -= valor
        registrar(dados, user, f"Saque R${valor:.2f}")
        print("✅ Saque feito")

    except:
        print("❌ Erro")

def historico(dados, user):
    print("\n📄 Histórico:")
    for h in dados[user]["historico"]:
        print("-", h)