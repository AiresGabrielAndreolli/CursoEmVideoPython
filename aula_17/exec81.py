nums = list()
while True:
    nums.append(int(input("Digite um número: ")))
    if nums[-1] == -10:
        nums.pop()
        break

print(f'A quantidade de números digitados foi {len(nums)}')
nums.sort(reverse=True)
print(*nums)
print('O numero 5 aparece na lista' if 5 in nums else 'O numero 5 não esta na lista')