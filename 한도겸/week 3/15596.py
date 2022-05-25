# 백준 15596번

sum = 0

a = [4,5,6,7,8,3,2,3,5,6,3,5,7,6]

def solve():
    global sum
    for x in a:
        sum += x
    return sum

print(solve())