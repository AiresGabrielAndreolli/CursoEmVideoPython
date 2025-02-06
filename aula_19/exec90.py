nome = str(input("Nome: "))
media = float(input("Média: "))
aluno = {
    'nome' : nome,
    'media' : media
}

aluno['situação final'] = 'Reprovado' if media < 6 else 'Aprovado'

for k, v in aluno.items():
    print(f'{k} é {v}')
