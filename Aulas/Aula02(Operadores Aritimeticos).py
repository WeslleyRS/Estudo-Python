########## OPERADORES ARITMÉTICOS ##########

# + (Adição)

# 5 + 2 == 7

# - (Subtração)

# 5 - 2 == 3

# * (Multiplicação)

# 5 * 2 == 10

# / (Divisão)

# 5 / 2 == 2,5

# ** (Potência)

# 5 ** 2 == 25

# // (Divisão Inteira)

# 5 // 2 == 2

# % (Resto da Divisão)


# 5 % 2 == 1

########## ORDEM DE PRECEDÊNCIA ##########

# 1 | ()

# 2 | ** (Potência)

# 3 | *(Multiplicação) / (Divisão) // (Divisão Inteira) % (Resto da Divisão)

# 4 | + (Adição) - (Subtração)

########## EXEMPLOS ##########

#Em todos os Exemplos Seguiremos a Ordem de Precedência

## ex01 = 5 + 2 * 2 ##

#No Exemplo 01 (ex01) o Calculo será resolvido da seguinte forma 2 * 2 == 4 para depois fazermos 4 + 5 == 11

## ex02 = 3 * 5 + 4 ** 2 ##

#No Exemplo 02 (ex02) Calcularemos da mesma maneira que no ex01, seguiremos a Ordem de Precedência, então o problema será resolvido da seguinte maneira, primeiro faremos a potencialização dos números 4 ** 2 == 16 para depois fazermos a multiplicação 3 * 5 == 15 e então a soma que será 15 + 16 == 31

## ex03 = 3 * ( 5 + 4 ) ** 2 ##

#Já no Exemplo 03 (ex03) iremos iniciar pelos colchetes que no caso possuem a adição de 5 + 4 == 9 para depois realizarmos a potencialização de 9 ** 2 == 81 e 81 * 3 == 243

########## PRÁTICA ##########

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

pot = n1 ** n2

mut = n1 * n2

div = n1 / n2

Divin = n1 // n2 

Resdiv = n1 % n2

adi = n1 + n2

sub = n1 - n2
print (' A Potencia de {0} e {1} equivale a {2} \n já a Multiplicação {3} \n A Divisão {4} \n O Resto da Potecia {5} \n A Adição {6} \n E a Subtração {7} '.format (n1, n2, pot, mut, div, Divin, Resdiv, adi, sub))