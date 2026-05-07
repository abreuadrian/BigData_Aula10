#Atividade 02
from utilities.helper import time_clear
PESO = 100
MULTA = 4

def get_weight():
    """Captura um valor em float do usuário"""
    while True:
        try:
            x = float(input('Informe o peso de peixes pescados(kg): '))
            if x > 0:
                return x
            else:
                print('Erro. Informe um número válido')
        except ValueError: print('Erro. Informe um número válido')

def calc_multa(n):
    """Calcula o valor da multa (R$4/kg)"""
    return (n - PESO) * MULTA

def calc_excess(n):
    """Verifica se o valor em float informado é permitido ou excedido"""
    if n > PESO:
        return 'Peso excedido'
    else: return 'Peso permitido'

def continue_or_not():
    """Pergunta ao usuário se deseja inserir outro peso. 
    Solicita entrada 'S' ou 'N' em loop até obter uma resposta válida."""
    while True:
        opt = input('\nDeseja informar outro peso? (S/N): ').strip().lower()
        if opt == 'n':
            break
        if opt == 's':
            time_clear(0.7)
            display()

def display():
    """Controla o fluxo principal da aplicação.
    Captura o peso via get_weight(), exibe o resultado da verificação
    e, se houver multa, exibe o valor. Em seguida, pergunta ao usuário
    se deseja repetir o processo."""
    weight = get_weight()
    status = calc_excess(weight)
    time_clear(0.7)
    print(f'Peso: {weight} - {status}')
    if status == 'Peso excedido':
        print(f'Multa: R${calc_multa(weight):.2f}')
    time_clear(0.7)


while True:
    display()
    if not continue_or_not():
        time_clear(0.7)
        break