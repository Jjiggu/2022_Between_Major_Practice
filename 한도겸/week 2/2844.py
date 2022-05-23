# 백준 2884번

H = int(input(""))
M = int(input(""))

if M - 45 < 0:
    H -= 1
    if H - 1 < 0:
        H = 23
    M = 60 + (M - 45)
else:
    M -= 45

print(H, M)