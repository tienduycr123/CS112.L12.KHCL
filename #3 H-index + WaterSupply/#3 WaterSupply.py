def need(n,m):
    return n-m-1

def case(n,m):
    if m == 0 | m == n: return 1
    if m == 1: return n
    return case(n - 1, m - 1) + case(n - 1, m)


a = []
a = list(map(int, input().split()))

b = []
for i in range(a[1]):
    b.append([int(j) for j in input().split()])

print(b[0])

pipe_need = need(a[0], a[1])
print(pipe_need)
if pipe_need != 0:
    print(case(a[0]+1, pipe_need))
if pipe_need == 0:
    print(0)