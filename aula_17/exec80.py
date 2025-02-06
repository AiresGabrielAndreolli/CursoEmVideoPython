nums = list()

for i in range(0, 5):
    n = int(input("Digite um numero: "))
    if i == 0 or n > nums[-1]:
        nums.append(n)
    else:
        for pos in range(0, len(nums)):
            if n < nums[pos]:
                nums.insert(pos, n)
                break

print(*nums)