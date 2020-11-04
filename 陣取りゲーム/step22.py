#STEP: 22 陣取りのターン数
H,W,N=[int(i) for i in input().split()]

s=[]
for i in range(H):
    line = input()
    for j in range(W):
        if line[j] == '*':
            sy = i
            sx = j
            break
    s.append(list(line))

l=[int(input()) for i in range(N)]


def addJinti(y,x,cnt,l):
    cnt+=1
    jin=[]
    if x != 0 and s[y][x-1] == ".":
        if l.count(cnt)==0:
            s[y][x - 1] = '*'
        else:
            s[y][x - 1] = '?'
            
        jin.append([y,x-1])
    if x != W-1 and s[y][x + 1] == ".":
        if l.count(cnt)==0:
            s[y][x + 1] = '*'
        else:
            s[y][x + 1] = '?'
        jin.append([y,x+1])
    if y != 0 and s[y-1][x] == ".":
        if l.count(cnt)==0:
            s[y - 1][x] = '*'
        else:
            s[y - 1][x] = '?'
        jin.append([y-1,x])
    if y != H-1 and s[y+1][x] == ".":
        if l.count(cnt)==0:
            s[y + 1][x] = '*'
        else:
            s[y + 1][x] = '?'
        jin.append([y+1,x])
    return jin


cnt=0
que=[]
que.append([sy,sx])

if l.count(0)==0:
    s[sy][sx] = '*'
else:
    s[sy][sx] = '?'

for k in range(H*W):
    jin=[]
    for i in que:
        my,mx=i
        jin+=addJinti(my,mx,cnt,l)
    que=jin
    cnt+=1


for i in s:
    print("".join(i))
