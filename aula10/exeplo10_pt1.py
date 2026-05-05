import utilities

#Ex01.: Tratamento de erro
def ex01():
    print(' ===== Cálculo de produtividade =====\n')
    while True: 
        try:
            total_produzido = float(input('Informe o valor total da venda: R$'))
            funcionarios = int(input('Informe o total de funcionários: '))

            media_funcionario = total_produzido / funcionarios

            print(f'\nMédia por funcionário: R${media_funcionario:.2f}')
            break
        except ValueError: 
                print('\nErro. Informe um valor válido.')
                utilities.time_clear(1.5)
        except ZeroDivisionError:
                print('\nInforme um número de funcionários válido.')
                utilities.time_clear(1.5)

ex01()

