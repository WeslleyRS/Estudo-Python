usuario = input('Digite seu úsuario: ')

print (f'Seja bem vindo(a) ao sistema de notas {usuario}!')

semestre1 = float (input ('Insira a nota do primeiro semestre: '))

semestre2 = float (input ('Insira a nota do segundo semestre: '))

semestre3 = float (input ('Insira a nota do terceiro semestre: '))

semestre4 = float (input ('Insira a nota do quarto semestre: '))

nota_total = semestre1 + semestre2 + semestre3 + semestre4

media_semestre = nota_total / 4

print (f'A sua nota total é de {nota_total} e sua media por semestre é de {media_semestre}')
