while True:
    n = int(input('Digite o num para tabuada (para sair digite um numero negativo): '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')