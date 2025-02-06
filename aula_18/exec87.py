matriz = [

        [], [], [],
        [], [], [],
        [], [], []
]

somaPares = somaTercCol = 0

for i in range(0, 9):
    num = int(input("Digite um número: "))
    matriz[0].append(num) if i < 3 else matriz[1].append(num) if i < 6 else matriz[2].append(num)
    if num % 2 == 0:
        somaPares += num

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]}', end='  ')
        if j == 2:
            somaTercCol += matriz[i][j]
    print()

maior = max(matriz[1])

print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTercCol}')
print(f'O maior valor da segunda linha é {maior}')
