a = int(input())
b = int(input())

c1 = a * (b % 10)
c2 = a * (b % 100 // 10)
c3 = a * (b // 100)

print(c1, c2, c3, a * b, sep = '\n')