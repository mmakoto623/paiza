#STEP: 37 区間への足し算(累積和を用いた imos法)
N,M = map(int,input().split())
A = list(map(int,input().split()))

add=[0 for i in range(N+2)]

for i in range(M):
    l,u,a = map(int,input().split())
    l-=1
    u-=1
    add[l]+=a
    add[u+1]-=a

for i in range(N):
    print(A[i]+add[i])
    add[i+1]+=add[i]
