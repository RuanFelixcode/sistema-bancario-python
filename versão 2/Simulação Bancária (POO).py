class ContaBancaria:
    def __init__(self):
        self.titular = ''
        self.saldo = 0.0
        self.limite = 0.0

    def cadastrar_usuario(self):
        while True:
            nome = input('digite seu nome:')
            if not nome.replace(' ','').isalpha():
                print('so aceitamos nomes simples ou compostos')
                continue
            self.titular = nome
            break

    def mostrar_info(self):
        print(f'usuario:{self.titular}\nsaldo:{self.saldo}\nlimite do cartao:{self.limite}')

    def depositar(self):
        if self.titular == '':
            print('cadastre um nome de usuario primeiro')
            self.cadastrar_usuario()
        
        while True:
            try:
                depositar = float(input('digite o valor do deposito:'))
                if depositar < 0:
                    print('nao e permitido valor negativo')
                    continue
                else:
                    self.saldo += depositar
                    self.limite = self.saldo
                
                while True:
                    print('deseja depositar novamente?(s pra sim e n pra nao):')
                    opc = input('selecione uma opçao:').lower()
                    if opc == 'n':
                        return
                    elif opc == 's':
                        break
                    else:
                        print('opçao invalida')
                        continue
            except ValueError:
                print('digite apenas numeros exemplos 1,2,3,4,5')

    def sacar(self):
        if self.titular == '':
            print('cadastre um nome de usuario primeiro')
            self.cadastrar_usuario()
        
        while True:
            try:
                saque = float(input('digite o valor do saque:'))
                if saque > self.saldo:
                    if saque > self.saldo + self.limite:
                        print('valor do saque ultrapasa o limite do cartão')
                        break
                    else:
                        restante = saque - self.saldo
                        self.saldo = 0
                        self.limite -= restante
                else:
                    self.saldo -= saque
                    self.limite = self.saldo
                    
                while True:
                    print('deseja sacar novamente?(s pra sim e n pra nao):')
                    opc = input('selecione uma opçao:').lower()
                    if opc == 'n':
                        return
                    elif opc == 's':
                        break
                    else:
                        print('opçao invalida')
                        continue
            except ValueError:
                print('digite apenas valores numericos exemplos 1,2,3,4,5')

    def transferencia(self, destinatario):
        if self.titular == '':
            print('cadastre um nome de usuario primeiro')
            self.cadastrar_usuario()
        
        while True:
            try:
                trasferir = float(input(f'digite o valor para ser trasferido ao usuario {destinatario.titular} R$:'))
                if trasferir > self.saldo:
                    if trasferir > self.saldo + self.limite:
                        print('valor da transferencia ultrapasa o limite do cartão')
                        break
                    else:
                        destinatario.saldo += trasferir
                        trasferir -= self.saldo
                        self.saldo = 0
                        self.limite -= trasferir
                        
                else:
                    self.saldo -= trasferir
                    destinatario.saldo += trasferir
                    self.limite = self.saldo
                    
                while True:
                    opc = input('deseja transferir novamente?(s pra sim e n pra nao):').lower()
                    if opc == 'n':
                        return
                    elif opc == 's':
                        break
                    else:
                        print('opção inválida')
                        continue

            except ValueError:
                 print('Erro: entrada inválida. Use apenas números (ex: 10, 25.5).')
                
                


usuario1 = ContaBancaria()
usuario1.mostrar_info()
usuario1.cadastrar_usuario()
usuario1.depositar()
usuario1.mostrar_info()
usuario1.sacar()
usuario1.mostrar_info()
print('-='*30)
usuario2 = ContaBancaria ()
usuario2.cadastrar_usuario()
usuario2.mostrar_info()
usuario1.transferencia(usuario2)
usuario2.mostrar_info()
print('-='*30)
usuario1.mostrar_info()


