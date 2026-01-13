########## UTILIZANDO MÓDULOS ##########

########## math ##########  

# Para importar a biblioteca inteira dar o seguinte comando: (import math)

#   ceil: Faz um arredondamento para cima
#   floor: Faz um arredondamento para baixo
#   trunc: Ele vai eliminar o numero da virgula para frente
#   pow: Potência
#   sqrt: calcular a Raiz Quadrada 
#   factorial: calculo de factoriais

#  Caso queira importar apenas uma determinada secção da biblioteca deve se usar o seguinte código

    #  from math import sqrt
    #  from matg import ceil

# Este é um dos exemplos para importar determinados ramos da biblioteca

import math

valor = int(input('Digite um número: '))

raiz = math.sqrt(valor)

print (f' A raiz de {valor} é igual a {raiz}')

from math import factorial

valor1 = int (input('Digite um valor: '))

factorial = math.factorial(valor1)

print (f'O valor factorial de {valor1} é de {factorial}')