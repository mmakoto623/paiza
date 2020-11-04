#STEP: 21 陣取りの手間
H,W=[int(i) for i in input().split()]

s=[]
for i in range(H):
    line = input()
    for j in range(W):
        if line[j] == '*':
            sy = i
            sx = j
            break
    s.append(list(line))


def addJinti(y,x,cnt):
    cnt+=1
    jin=[]
    if x != 0 and s[y][x-1] == ".":
        s[y][x - 1] = str(cnt)
        jin.append([y,x-1])
    if x != W-1 and s[y][x + 1] == ".":
        s[y][x + 1] = str(cnt)
        jin.append([y,x+1])
    if y != 0 and s[y-1][x] == ".":
        s[y - 1][x] = str(cnt)
        jin.append([y-1,x])
    if y != H-1 and s[y+1][x] == ".":
        s[y + 1][x] = str(cnt)
        jin.append([y+1,x])
    return jin

s[sy][sx] = '0'
cnt=0
que=[]
que.append([sy,sx])

for k in range(H*W):
    jin=[]
    for i in que:
        my,mx=i
        jin+=addJinti(my,mx,cnt)
    que=jin
    cnt+=1


for i in s:
    print("".join(i))
