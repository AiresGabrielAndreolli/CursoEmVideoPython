nums = list()

while True:
    nums.append(int(input("Digite um numero: ")))
    if (nums[-1]) in nums[:-1]:
        nums.pop()
    if str(input("Continuar (S/N) ")).upper() == 'N':
        break

nums.sort()
print(*nums)