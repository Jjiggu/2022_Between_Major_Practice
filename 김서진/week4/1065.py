n = int(input())
if n < 100:
    count = n
else:
    count = 99
    for i in range(100, n + 1):
        if i//100 + i%10 == 2 * (i%100//10):
            count += 1

print(count)