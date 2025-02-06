qtdLegMaior = qtdHomem = qtdMulherMenorVint = 0
while True:

    idade = int(input("Digite a idade: "))
    while True:
        sexo = str(input("Digite o sexo (M/F): "))
        if sexo in 'MmFf':
            break
    if idade > 18:
        qtdLegMaior += 1
    if sexo in 'Mm':
        qtdHomem += 1
    if (sexo in 'Ff') and idade < 20:
        qtdMulherMenorVint += 1
    while True:
        continuar = str(input("Continuar? (S/N) "))
        if continuar in 'NnSs':
            break
    if continuar in 'Nn':
        break

print(f'+18 {qtdLegMaior}  Homens {qtdHomem}  Mulher -20 {qtdMulherMenorVint}')