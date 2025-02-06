pessoas = list()
maior = list()
menor = list()

while True:
    pessoa = list()
    pessoa.append((input("Digite o nome: ")))
    pessoa.append(float(input("Digite o peso: ")))
    pessoas.append(pessoa[:])
    continuar = str(input('Continuar?(S/N) '))
    if continuar in 'Nn':
        break

print(pessoas)

for i in range(0, len(pessoas)):
    if i == 0:
        menor.append(pessoas[i][:])
        maior.append(pessoas[i][:])
    elif pessoas[i][1] > maior[-1][1]:
        maior.clear()
        maior.append(pessoas[i][:])
    elif pessoas[i][1] < menor[-1][1]:
        menor.clear()
        menor.append(pessoas[i][:])
    elif pessoas[i][1] == maior[-1][1]:
        maior.append(pessoas[i][:])
    elif pessoas[i][1] == menor[-1][1]:
        menor.append(pessoas[i][:])

print(maior)

print(f'A quantidade de pessoas cadastradas foi {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior[0][1]}Kg. Peso de', end=' ')
for p in maior:
    print(f'[{p[0]}]', end=" ")
print()
print(f'O menor peso foi de {menor[0][1]}Kg. Peso de', end=' ')
for p in menor:
    print(f'[{p[0]}]', end=" ")
print()