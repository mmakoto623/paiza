N,M = map(int,input().split())
ab =[[int(i) for i in input().split()] for i in range(M)]

ans=[[0 for i in range(N)]  for i in range(N)]

for i in ab:
    a,b = i
    ans[b-1][a-1]=1
    ans[a-1][b-1]=1
    
for i in ans:
    for j in range(len(i)):
        print(i[j],end="")
    print("")
