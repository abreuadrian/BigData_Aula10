from utilities.helper import time_clear
#Ex02.: 
# for i in range(5):
#     total_produzido = float(input('Informe o valor total da venda: R$'))
#     funcionarios = int(input('Informe o total de funcionários: '))
#     media_funcionario = total_produzido / funcionarios

#     print(f'\nMédia por funcionário: R${media_funcionario:.2f}')

for i in range(5):
    try:
        total_produzido = float(input('Informe o valor total da venda: R$'))
        funcionarios = int(input('Informe o total de funcionários: '))
        media_funcionario = total_produzido / funcionarios

        print(f'\nMédia por funcionário: R${media_funcionario:.2f}')
    except ValueError: 
            print('\nErro. Informe um valor válido.')
            time_clear(1.5)
    except ZeroDivisionError:
            print('\nInforme um número de funcionários válido.')
            time_clear(1.5)
        