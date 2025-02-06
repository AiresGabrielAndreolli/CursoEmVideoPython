from random import randint

def somaPar(nums):
    soma = 0
    for n in nums:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {nums}, temos {soma} ')    
def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))

numeros = list()
sorteia(numeros)
somaPar(numeros)
