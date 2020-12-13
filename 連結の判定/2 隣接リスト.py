N,M = map(int,input().split())
ab =[[int(i) for i in input().split()] for i in range(M)]

ans=[[] for i in range(N)]

for i in ab:
    a,b = i
    ans[a-1].append((b-1))
    ans[b-1].append((a-1))

for i in ans:
    temp= sorted(i)
    for j in temp:
        print(j,end="")
    print("")
