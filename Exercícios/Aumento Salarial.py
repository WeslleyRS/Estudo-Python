usuario = input('Digite seu usuario: ')

print (f'Seja bem-vindo ao sistema de aumento {usuario}.')

salario = float (input('Digite o salário do funcionario: '))

porcentagem_aumento = int (input('Digite a porcentagem de aumento: '))

calculo_aumento =  int (salario * porcentagem_aumento / 100 + salario)

print (f'O salario atual do funcionario é de {salario} e a porcentagem de aumento é {porcentagem_aumento}% com isso o novo salário é de {calculo_aumento}')
