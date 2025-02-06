from random import randint

cont = 1

numRand = randint(1, 10)
num = int(input("Chute um número de 1 a 10: "))
while num != numRand:
    num = int(input("Chute um número de 1 a 10: "))
    cont += 1
print("Você acerto o número {} em {} tentativas.".format(numRand, cont))