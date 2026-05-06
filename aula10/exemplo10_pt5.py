#Ex05.:
try:
    total_produzido = float(input('Informe o valor total da venda: R$'))
    funcionarios = int(input('Informe o total de funcionários: '))
    media_funcionario = total_produzido / funcionarios

except Exception as e:
    print(f'Ops! ERRO do tipo: {e}.')
except KeyboardInterrupt:
    print('\nPrograma interrompido pelo usuário.')
else: 
    print(f'\nMédia por funcionário: R${media_funcionario:.2f}')

finally:  
    print('Programa Encerrado')
    