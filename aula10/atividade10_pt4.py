#Atividade 04
def get_nums():
    for i in range(3):
        print(f'=== {i+1}ª soma ===')
        n1 = int(input('Informe o 1º número: '))
        n2 = int(input('Informe o 2º número: '))
        print(verify_sum_even(n1, n2))
        print()

def verify_sum_even(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        summ = n1 + n2
        return f'{n1} + {n2} = {summ}'
    
    return f'Cálculo não realizado.({n1} + {n2}) Um ou mais números são ímpares.'

if __name__ == '__main__':
    get_nums()


