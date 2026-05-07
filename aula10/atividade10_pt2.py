#Atividade 02
from utilities.helper import time_clear #Colocar time clear

EMPLOYEE_QNT = 3

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name 
        self.salary = salary
        self.bonus = bonus 
        self.final_salary = salary + bonus
    
    def __str__(self):
        return f'Nome: {self.name} - Salário: R${self.salary:.2f} - Bônus: R${self.bonus:.2f}\nSalário Líquido: R${self.final_salary:.2f}'

def get_name():
    while True:
        name = input('Informe o nome do funcionário: ').capitalize()
        if name:
            return name
        else: 
            print('Insira um nome.')

def base_salary():
    while True:
        try:
            salary = float(input('Informe o salário: R$'))
            if salary > 0:
                return salary
            else: 
                print('Erro. Informe um valor válido.')
        except ValueError:
            print('Erro. Insira um valor válido')
    
def bonus_salary():
    while True:
        try:
            bonus = float(input('Informe o bônus: R$'))
            if bonus >= 0:
                return bonus
            else:
                print('Erro. Insira um bônus válido.')
        except ValueError:
            print('Erro. Insira um bônus válido.')

list_employers = []
for i in range(EMPLOYEE_QNT):
    name = get_name()
    salary = base_salary()
    bonus = bonus_salary()
    funcionario = Employee(name, salary, bonus)
    list_employers.append(funcionario)

for emp in list_employers:
      print(emp)
      print()