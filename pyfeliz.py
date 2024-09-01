menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_saque=0
sair = 0    

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if saldo > 0 or saldo == 0 :
            saldo += valor
            extrato += f'Saldo atualizado! R$:, {saldo:.2f} \n'

        else:
            print('Operação falhou! O valor é informado é indefinido, erro no deposito')

    elif opcao == "s":
        valor_saque= float(input('Informe o valor que será sacado: '))
        excedeu_saldo= valor_saque > saldo
        excedeu_saque= valor_saque >=LIMITE_SAQUES
        excedeu_limite= valor_saque> limite

        if  excedeu_saldo:
            print('Operação falhou, o saldo foi insuficiente')

        #
        elif valor_saque> limite:
            print('Operação falhou, o valor extrapola o limite')
    #
        elif numero_saques >=LIMITE_SAQUES:
            print('Operação falhou, a ação ultrapassa o valor de limite de saque')
    #
        elif valor_saque > 0:
            saldo-=valor_saque
            numero_saques+=1
            extrato+= f"saque realizado, valor {valor_saque:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    if opcao =="e":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


    elif opcao == "q":

        break