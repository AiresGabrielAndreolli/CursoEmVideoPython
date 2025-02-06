from datetime import date

anoAtual = date.today()
anoAtual = anoAtual.year

nome = str(input("Nome: "))
anoNasc = int(input("Ano Nascimento: "))
ctps = int(input("CPTS: ")) 

pessoa = {
    'nome' : nome,
    'idade' : anoAtual - anoNasc,
    'ctps' : ctps
}

if ctps:
    pessoa['ano contratacao'] = int(input("Ano contratação: "))
    pessoa['salario'] = float(input("Salário: "))
    aposenta = pessoa['idade'] + 35
    pessoa['idade aposentadoria'] = aposenta if aposenta > 64 else 64

print(pessoa)