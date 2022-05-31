# 백준 1065번
n = int(input())
if n < 100:
    count = n
else:
    count = 99

    for x in range(100, n + 1):
        calList = list(map(int, list(str(x))))
        if calList[1] - calList[0] == calList[2] - calList[1]:
            count += 1

print(count)