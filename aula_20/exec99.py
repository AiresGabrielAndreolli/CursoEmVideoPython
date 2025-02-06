def maior(*num):
    print('-='*20)
    print('Analisando os valores ...')
    for pos, n in enumerate(num):
        if pos == 0:
            maior = n
        if n > maior:
            maior = n
        print(n, end=' ')
    print(f'foram informados. {len(num)} valores ao todo.')
    print(f'O maior número é {maior}')
    
maior(5,4,2)
maior(3, 5 , 43, 9)