def linha():
    print('-='*20)

pessoas = []
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: ')).strip().upper()
        if sexo in 'MF':
            break
        print('Sexo invalido! Tente de novo! ', end='')
    idade = int(input('Idade: '))
    
    pessoa = {
        'nome' : nome,
        'sexo' : sexo,
        'idade' : idade
    }

    pessoas.append(pessoa.copy())

    continuar = str(input('Continuar? (S/N) ')).strip().upper()
    if continuar == 'N':
        break

somaIdade = 0
qtdPes = len(pessoas)
mulheres = []
acimaMedia = []
for p in pessoas:
    somaIdade += p['idade']

media = somaIdade/qtdPes

for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p.copy())
    if p['idade'] > media:
        acimaMedia.append(p.copy())

linha()

print(f'- O grupo tem {qtdPes} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m['nome'], end=' ')
print()
print('- A lista de pessoas que estão acima da média:')
for p in acimaMedia:
    for k, v in p.items():
        print(f'\t{k} = {v}', end='; ')
    print()
print('<< ENCERRADO >>')