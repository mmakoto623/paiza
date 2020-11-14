#STEP: 36 最長の区間
N,M= map(int,input().split())
A = list(map(int,input().split()))

front=0
back=0
anscnt=-1
goukei=A[front]

while True:
    if goukei > M:
        goukei -=A[back]
        back+=1
    else:
        front+=1
        anscnt = max(anscnt,front - back)
        if front == N:
            break
        goukei += A[front]

print(anscnt)
