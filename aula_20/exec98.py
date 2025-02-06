def linha(carac, tam):
    print(carac*tam)
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if (inicio > fim and passo > 0):
        passo = -passo
    
    linha('-=', 20)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    for i in range(fim if (inicio < fim and passo < 0) else inicio, inicio + (1 if passo > 0 else -1) if (inicio < fim and passo < 0) else fim + (1 if passo > 0 else -1), passo):
        print(i, end=' ', flush=True)
    print()
'''
versao do prof

from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
'''
contador(1, 10, 1)
contador(10, 0, 2)
linha('-=', 20)
print('Personalize!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)