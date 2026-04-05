# ================================
# 💻 SISTEMA DE CAIXA ELETRÔNICO
# ================================

# validar a senha
senha = int(input('Digite a senha: '))

while True:
    if senha == 1234:
        break
    senha = int(input('Senha inválida, digite novamente: '))

# saldo inicial
saldo_at = 0

print('''\n=== MENU DE OPÇÕES ===
[1] Depositar
[2] Sacar
[3] Consultar saldo
[4] Sair''')

opc = int(input('Selecione a opção: '))

# loop principal
while True:
    
    # depósito
    if opc == 1:
        deposito = float(input('Quanto deseja depositar? R$ '))
        saldo_at += deposito
        print(f'Depósito realizado! Saldo atual: R$ {saldo_at:.2f}')
    
    # saque
    elif opc == 2:
        saque = float(input('Quanto deseja sacar? R$ '))
        
        if saque > saldo_at:
            print('❌ Saldo insuficiente!')
        else:
            saldo_at -= saque
            print(f'💸 Saque realizado! Saldo atual: R$ {saldo_at:.2f}')
    
    # consultar saldo
    elif opc == 3:
        print(f'💰 Seu saldo atual é: R$ {saldo_at:.2f}')
    
    # sair
    elif opc == 4:
        print('Encerrando o sistema...')
        break
    
    # opção inválida
    else:
        print('⚠️ Opção inválida, tente novamente.')

    # mostrar menu novamente
    print('''\n=== MENU DE OPÇÕES ===
[1] Depositar
[2] Sacar
[3] Consultar saldo
[4] Sair''')
    
    opc = int(input('Selecione a opção: '))

print('Fim do programa.')
