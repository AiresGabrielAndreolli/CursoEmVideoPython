teste = list()
teste.append('Gabriel')
teste.append(16)

galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

del teste, galera

teste = list()
teste.append('Gabriel')
teste.append(16)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

del teste, galera

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[3][1])

for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos')

del galera

galera = list()
dado = list()
qtdMaior = qtdMenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        qtdMaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        qtdMenor += 1
print(f'Temos {qtdMaior} maiores e {qtdMenor} menores')

del galera, dado