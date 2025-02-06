n = s= 0 
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
#print("asomavale {}".format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
salario = 987
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print('O {} tem {} anos e ganha R${:.2f}'. format(nome, idade, salario))
print('O %s tem %d anos e ganha R$%.2f}' % (nome, idade, salario)) #antiquado