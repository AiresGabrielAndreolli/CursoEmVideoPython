'''for i in range(1, 10):
    print(i)
print("Fim")'''

'''i=1
while i < 10:
    print(i)
    i += 1
print('fim')'''

'''num = 1
while num != 0:
    num = int(input("Digite um valor: "))
print("Fim")'''

par = impar = 0
n = -1
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n%2 == 0:
            par +=1
        else:
            impar += 1
print("Qtd impar {} __________ Qtd par {}".format(impar, par))