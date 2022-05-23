h, m = int(input().split())

real_time = 60 * h + m
now_h = (real_time - 45) // 60
now_m = (real_time - 45) % 60

print(now_h, now_m)