#Atividade 01

from utilities.helper import time_clear
import os 

saldo = 1000

def display_saldo():
    print(f'Saldo total: R${saldo}')

def sacar():
    while True: 
        try:
            x = float(input('Informe o valor do saque: R$'))
            time_clear(1)
        except Exception as e: 
            time_clear(1)
            print('Erro. Insira um número válido\n')
        else: 
            return x

def verify_sacar(saque):
    global saldo
    if saque > saldo:
        print('Saldo insuficiente.\n')
    elif saque < 0:
        print('Informe um número válido.\n')
    else: 
        return saque

def new_saldo_sacar(saque):
    global saldo
    saldo -= saque
    return saldo

def depositar():
    while True: 
        try:
            x = float(input('Informe o valor do depósito: R$'))
            time_clear(1)
        except Exception as e: 
            time_clear(1)
            print('Erro. Insira um número válido\n')
        else: return x

def verify_depositar(deposito):
    if deposito <= 0:
        print('Erro. Insira um depósito válido\n')
    else:
        return deposito
    
def new_saldo_depositar(deposito):
    global saldo
    saldo += deposito
    return saldo 

def sair():
    print('Encerrando programa...')
    time_clear(1.5)
    print('Programa encerrado. Volte sempre!')


def menu():
    dict_opt = {1: "Mostrar Saldo",
                2: "Sacar",
                3: "Depositar",
                4: "Sair"}
    return dict_opt

def get_menu_choice(options):
    for i, c in options.items(): 
        print(f'[{i}] - {c}')
    opt = input('\nSelecione sua opção: ')
    time_clear(1)
    return opt

def run_menu_choice(option):
    match option: 
        case '1':
            display_saldo()
            continue_or_not()
        case '2':
            while True:
                saque = sacar()
                if verify_sacar(saque): 
                    break
            new_saldo_sacar(saque)
            print(f'Saque realizado: R${saque:.2f} - Saldo disponível: R${saldo:.2f}')
            continue_or_not()
        case '3':
            while True:
                deposito = depositar()
                if verify_depositar(deposito): 
                    break
            new_saldo_depositar(deposito)
            print(f'Deposito realizado: R${deposito:.2f} - Saldo disponível: R${saldo:.2f}')
            continue_or_not()
        case '4':
            sair()
        case _:
            print('Erro')
            continue_or_not()

def continue_or_not():
    while True: 
        opt = input('\nDeseja continuar? (S/N): ').strip().lower()
        if opt in ['sim', 's', 'ss']:
            time_clear(1)
            run()
        elif opt in ['nao', 'não', 'nn', 'n']:
            break
        else: 
            time_clear(1)
            print('Informe uma opção válida.')
    sair()

def run():
    options = menu()
    get_choice = get_menu_choice(options)
    run_menu_choice(get_choice)

if __name__ == '__main__':
    os.system('cls')
    run()
    