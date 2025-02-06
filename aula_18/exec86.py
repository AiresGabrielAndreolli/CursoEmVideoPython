matriz = [

        [], [], [],
        [], [], [],
        [], [], []
]

for i in range(0, 9):
    num = int(input("Digite um número: "))
    matriz[0].append(num) if i < 3 else matriz[1].append(num) if i < 6 else matriz[2].append(num)


for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]}', end='  ')
    print()
