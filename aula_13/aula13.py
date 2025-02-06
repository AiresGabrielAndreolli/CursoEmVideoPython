'''
ini = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

for i in range(ini, fim+1, passo): #range(0 -> começo , 7 -> fim , 2 -> passo (-1))
    print(i)
'''
s = 0
for i in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print("O somatorio dos valores É {}".format(s))
