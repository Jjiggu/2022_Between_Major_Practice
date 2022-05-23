"""
a =  int(input())
b =  int(input())

b1 = b//100
b2 = (b - b1*100)//10
b3 = b % 10
result = a * b

print(b3*a)
print(b2*a)
print(b1*a)
print(result)
"""
a = int(input())
b = int(input())
print(a * (b % 10))
print(a * ((b//10)%10))
print(a * int(b/100))
print(a*b)