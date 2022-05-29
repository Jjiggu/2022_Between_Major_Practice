#백준 4673번 답지
def calculate(n):
    n = n + sum(map(int, str(n)))
    return n


notSelfnumber = set()

for a in range(1, 10001):
    notSelfnumber.add(calculate(a))

for b in range(1, 10001):
    if b not in notSelfnumber:
        print(b)