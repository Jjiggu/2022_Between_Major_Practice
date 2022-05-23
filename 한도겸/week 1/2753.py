# 백준 2753번

x = int(input("년도를 입력하시요: "))

if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
    print(1)
else:
    print(0)