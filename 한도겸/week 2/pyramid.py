# 피라미드 모양으로 별 출력

a = 5
b = 1

for x in range(6):
    print(" " * a, "*" * b, sep="")
    a -= 1
    b += 2