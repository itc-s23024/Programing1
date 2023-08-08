n = int(input())
listb = [0] * n

for i in range(n):
    listb[i] = input()

for i in range(n - 1):
    for j in range(n - 1):
        if listb[j] < listb[j + 1]:
            tmp = listb[j]
            listb[j] = listb[j + 1]
            listb[j + 1] = tmp

result = " ".join(listb)
print(result)
