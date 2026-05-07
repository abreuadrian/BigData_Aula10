#Atividade 05
from utilities.helper import time_clear

class Seller:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
        self.total_sales = calc_tot_sales(self.sales)
        self.med_sales = calc_med_sales(self.sales)

    def __str__(self):
         return f'Vendedor {self.name}\n\nTotal vendido: R${self.total_sales:.2f}\nMédia por venda: R${self.med_sales:.2f}'
    
def get_seller_name():
    name = input('Informe o nome do vendedor: ').capitalize()
    return name

def get_qnt_sales():
    while True:
        try:
            sales_qnt = int(input('Quantas vendas o vendedor fez? '))
            if sales_qnt > 0:
                return sales_qnt
            time_clear(1)
            print('Erro. Insira um número válido.')
        except ValueError:
            time_clear(1)
            print('Erro. Insira um número válido.')

def get_value_sales(n_sales):
    sales = []
    for i in range(n_sales):
        while True:
            try:
                sale = float(input(F'Informe o valor da {i+1}ª venda: R$'))
                if sale >= 1:
                    sales.append(sale)
                    break
                time_clear(1)
                print('Erro. Insira um número válido.')
            except ValueError:
                time_clear(1)
                print('Erro. Insira um número válido.')
    return sales

def calc_tot_sales (sales):
    return sum(sales)

def calc_med_sales(sales):
    return sum(sales) / len(sales)

def continue_or_not():
    while True:
        option = input('\nDeseja cadastrar outro vendedor? (S/N): ').strip().lower()
        if option in ['s', 'sim', 'ss']:
            return True

        if option in ['n', 'nao', 'não']:
            return False
        else: print('Erro. Informe uma opção válida.')

def main():
    sellers = []
    while True:
        time_clear(0.5)
        name = get_seller_name()
        time_clear(1)
        qnt_sales = get_qnt_sales()
        sales = get_value_sales(qnt_sales)
        time_clear(1)
        seller = Seller(name, sales)
        print(seller)
        sellers.append(seller)
        if not continue_or_not():
            break
    time_clear(1)
    print('Preparando relatório completo...')
    time_clear(1)
    print('Aguarde...')
    time_clear(1)
    for i in sellers:
        print(i)
        print()


if __name__ == '__main__':
    main()


