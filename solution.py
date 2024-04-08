def f(x):
    res = 0
    for i in range(100):
        a = 5
        for j in range(i):
            a *= 5
        delta = x // a
        if delta == 0:
            return res
        res += delta

q = int(input())
l, r = 0, 10**18
while l + 1 != r:
    m = (r+l)//2
    if f(m) < q:
        l = m
    else:
        r = m
if f(r) == q:
    print(r)
else:
    print('No solution')