def dn():
    self_num = set(range(1,10001))
    generate_num = set()

    for i in range(1,10001):
        for j in str(i):
            i += int(j)
        generate_num.add(i)

    self_num = self_num - generate_num

    for k in sorted(range(self_num)):
        print(k)