def linha():
    print('-'*30)
def titulo(texto):
    linha()
    print(texto)
    linha()
def soma(a, b):
    print(f'a = {a} e b = {b}')
    print(f'a soma é {a + b}')
def contador(*num):   #varios paramentros ou desempacotqamento
    for v in num:
        print(f'{v}', end=' ')
    print(f'recebi os valores {num} e são {len(num)}')
def dobra(lista):     #lista
    for pos, v in enumerate(lista):
        lista[pos] = v*2


titulo('   Curso em video')
titulo('   Aprenda python')
titulo('   Gustavo Guanabara')

soma(a=4, b=5)
soma(b=3, a=4)
soma(9, 0)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [7, 5, 9, 0]
dobra(valores)
print(valores)