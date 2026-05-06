#Atividade 01
saldo = 1000

def saque():
    while True:
        try:
            n = float(input('Informe o valor do saque: R$'))
        except ValueError:
            print('Erro. Insira um número válido. ')
        else: 
            return n

def verify_saque(n):
    if n > saldo:
        print('Saldo insuficiente.')
    elif n <= 0:
        print('Digite um número maior que 0.')
    else: 
        return n
        
def calc_total(saque):
    return saldo - saque

def display(saque, novo_saldo):
    print(f'\nFoi sacado R${saque:.2f} e restou R${novo_saldo:.2f} na conta')

while True:
    n = saque()
    if verify_saque(n):
        break
total = calc_total(n)

display(n, total)
