lista = list()
notas = list()

while True:
    nome = str(input('Digite o nome: '))
    notas.append(nome)
    notas.append(int(input('Digite a primeira nota: ')))
    notas.append(int(input('Digite a segunda nota: ')))
    notas.append((notas[1] + notas[2]) / 2)
    continuar = str(input('Continuar? (S/N) ')).strip().upper()
    lista.append(notas[:])
    notas.clear()
    if continuar == 'N':
        break
    
    

print('Nome - Nota 1 - Nota 2 - Média')
for i in range(0, len(lista)):
    for j in range(0, 4):
        print(lista[i][j], end='  ')
    print()


while True:
    alunoEspsn = str(input('Você quer algum aluno específico? (S/N) ')).strip().upper()
    if alunoEspsn == 'N':
        break
    while True:
        temAluno = 'N'
        alunoEsp = str(input('Qual aluno deseja? '))
        for aluno in lista:
            if alunoEsp in aluno[0]:
                temAluno = 'S'
        if temAluno == 'S':
            break
        print(f'O aluno {alunoEsp} não existe! Tente novamente...')

    for aluno in lista:
        if alunoEsp in aluno[0]:
            print(*aluno)