num = int(input())
hansu_num = 0

for i in range(1, num+1):
    if i < 100:
        hansu_num += 1
    else :
        num_list = list(map(int, str(i)))
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            hansu_num += 1

print(hansu_num)