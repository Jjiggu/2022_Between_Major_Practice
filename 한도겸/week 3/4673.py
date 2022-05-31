# 백준 4673번

print(1)
for number in range(2, 10001):
    self_numbers = False
    b = 1
    while b < number:
        if b // 10 == 0:
            self_number = b + b
        elif b // 100 == 0:
            self_number = b + b // 10 + b % 10
        elif b // 1000 == 0:
            self_number = b + b // 100 + (b // 10) % 10 + b % 10
        elif b // 10000 == 0:
            self_number = b + b // 1000 + (b // 100) % 10 + (b // 10) % 10 + b % 10
        else:
            self_number = 10001

        b += 1

        if number == self_number:
            self_numbers = False
            break
        else:
            self_numbers = True
    if self_numbers == True:
        print(number)