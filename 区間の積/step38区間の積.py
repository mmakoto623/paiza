#step38 区間の積

N,M= map(int,input().split())
A = list(map(int,input().split()))

front=0
back=0
anscnt=10**5
goukei=A[front]
flg = True

while flg:
    if goukei >= M:
        anscnt = min(anscnt,front - back + 1)
        goukei /=A[back]
        back+=1
        if back>front:
            flg=False
            break
    else:
        front+=1
        if front == N:
            flg = False
        else:
            goukei *= A[front]

    if goukei==0:
        while True:
            front+=1
            if front == N:
                flg=False
                break
            back=front
            goukei=A[front]
            if goukei!=0:
                break
    
if anscnt == 10**5:
    print(-1)
else:
    print(anscnt)