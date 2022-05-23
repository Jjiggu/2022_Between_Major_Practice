a, b = map(int, input().split())
if b == 45:
    b = 0
elif b < 45:
    if a == 0:
        b = b + 60 - 45
        a = 23
    else:
        b = b + 60 - 45
        a = a - 1
else:
    b = b - 45

print(a, b)