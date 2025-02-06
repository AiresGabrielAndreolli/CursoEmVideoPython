# lanche = (0, 1, 2, 3)
# print(lanche(0:2)) -> 01
# print(lanche(1:)) -> 123
# print(lanche(-1)) -> 3
# print(lanche(-2)) -> 2
# len(lanche) -> 4
''' 
for c(omida) in lanche:
    print(c)
Saida -> 0
         1
         2
         3
'''
# As tuplas são imutaveis
# nao tem como trocar (0, 1, 2, 3) por (0, 1, 2, 4)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3]) #desconsidera 3
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

# As tuplas são imutaveis
#lanche[1] = 'Refrigerante' -> erro
#print(lanche[1])


for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print("Comi muito")

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2, 4))

pessoa = ('Gabriel', 39, 'M', 115)
del(pessoa) #pode
del(pessoa[0]) #não pode
print(pessoa)