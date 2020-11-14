#STEP: 35 最短区間
N,M= map(int,input().split())
A = list(map(int,input().split()))

front=0
back=0
anscnt=10**5
goukei=A[front]

while True:
    if goukei >= M:
        anscnt = min(anscnt,front - back + 1)
        goukei -=A[back]
        back+=1
    else:
        front+=1
        if front == N:
            break
        goukei += A[front]

if anscnt == 10**5:
    print(-1)
else:
    print(anscnt)
