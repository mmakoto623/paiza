#STEP: 25 リバーシの操作（縦横）

H,W,Y,X = [int(i) for i in input().split()]
s=[list(input()) for i in range(H)]

def yoko(y,x):
    mx = -1
    for i in range(x+1,W):
        if s[y][i] == '*':
            mx = i
            break
    if mx > x and mx != -1:
        for i in range(x+1,mx):
            s[y][i] = '*'
    
    mx = -1
    for i in range(x-1,-1,-1):
        if s[y][i] == '*':
            mx = i
            break
    if mx < x and mx != -1:
        for i in range(mx,x):
            s[y][i] = '*'

def tate(y,x):
    my = -1
    for i in range(y+1,H):
        if s[i][x] == '*':
            my = i
            break
    if my > y and my != -1:
        for i in range(y+1,my):
            s[i][x] = '*'
    
    my = -1
    for i in range(y-1,-1,-1):
        if s[i][x] == '*':
            my = i
            break
    if my < y and my != -1:
        for i in range(my,y):
            s[i][x] = '*'

s[Y][X] = '*'
yoko(Y,X)
tate(Y,X)

for i in s:
    print("".join(i))