parenteses = list()
exp = str(input("Digite a expressão: "))
for carac in exp:
    if carac == '(':
        parenteses.append(carac)
    elif carac == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(carac)
            break

print('Expressão', 'inválida!' if len(parenteses) else 'válida!')