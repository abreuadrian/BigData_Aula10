#Ex06.:
def calc_med(n):
    tot = sum(n)
    med = tot/ len(n)
    return tot, med 

count = 1
while True:
    print(f'{count}º aluno\n')
    name = input('Nome do aluno: ').capitalize()

    lis_notes = []
    try: 
        for i in range(4):
            grade = float(input(f'Informe a {i+1}ª nota: '))
            lis_notes.append(grade)
    except ValueError:
        print('ERRO. Insira uma nota válida')
    else:
        total, media = calc_med(lis_notes)

        print(f'\nAluno: {name}')
        print(f'Total de pontos: {total}')
        print(f'Média: {media}')

    finally: 
        print('\nProcesso finalizado.')

    opt = input('\nDeseja calcular para outro aluno?(S/N)').strip().upper()
    print()
    if opt != 'S':
        break
    
    count += 1
print('Progama encerrado')