idadeTotal = 0
maior = -1
menosVinte = 0

for i in range(0, 4):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo (F/M): "))
    if sexo == 'M':    
        if idade > maior:
            maior = idade
    if sexo == 'F':
        if idade < 20:
            menosVinte+=1
    idadeTotal += idade
print("A media da idade do grupo é: ", idadeTotal/4)
print("A maior idade de um homem é (obs: se for -1 é pq nenhum homem foi cadastrado): ", maior)
print("A quantidade de mulheres com menos de 20 anos é: ", menosVinte)