#STEP: 26  裏返せる可能性（斜め）

H,W,Y,X = [int(i) for i in input().split()]

def naname(y,x):
    #右上
    if y!=0 and x!=W-1:
        my = y
        for mx in range(x+1,W):
            my-=1
            if my >= 0:
                if s[my][mx] != '*':
                    s[my][mx] = '*'
    #右下
    if y!=H-1 and x!=W-1:
        my = y
        for mx in range(x+1,W):
            my+=1
            if my <= H-1:
                if s[my][mx] != '*':
                    s[my][mx] = '*'
    
    #左上
    if y!=0 and x!=0:
        my=y
        for mx in range(x-1,-1,-1):
            my-=1
            if my >= 0:
                if s[my][mx] != '*':
                    s[my][mx] = '*'

    #左下
    if y!=H-1 and x!=0:
        my =y
        for mx in range(x-1,-1,-1):
            my+=1
            if my <= H-1:
                if s[my][mx] != '*':
                    s[my][mx] = '*'


s=[]
for i in range(H):
    tmp=''
    for j in range(W):
        tmp+='.'
    s.append(list(tmp))


s[Y][X] = '!'
naname(Y,X)

for i in s:
    print("".join(i))