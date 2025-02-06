from random import randint

numAle = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for pos, num in enumerate(numAle):
    if pos == 0:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(*numAle)

print(f'O maior é {maior} e o menor é {menor}')
print(f'O maior é {max(numAle)} e o menor é {min(numAle)}')