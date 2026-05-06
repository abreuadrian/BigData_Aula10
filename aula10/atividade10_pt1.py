#Atividade 01
SALDO = 1000
def saque():
    while True:
        try:
            n = float(input('Informe o valor do saque: R$'))
            if n > SALDO:
                print('Saldo insuficiente.')
                continue
            if n > 0:
                return n
            else: 
                print('Digite um número maior que 0.')
        except ValueError:
            print('Erro. Insira um número válido. ')

def calc_total(saque):
        return SALDO - saque

def display(saque, novo_saldo):
    print(f'Foi sacado R${saque:.2f} e restou R${novo_saldo:.2f} na conta')

n = saque()
total = calc_total(n)

display(n, total)
