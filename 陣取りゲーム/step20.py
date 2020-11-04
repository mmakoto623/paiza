#STEP: 20 陣取りの結末

def addJinti(y,x):
    if x != 0 and s[y][x-1] == ".":
        s[y][x - 1] = "*"
        x -= 1
        addJinti(y,x)
    if x != W-1 and s[y][x + 1] == ".":
        s[y][x + 1] = "*"
        x += 1
        addJinti(y, x)
    if y != 0 and s[y-1][x] == ".":
        s[y - 1][x] = "*"
        y -= 1
        addJinti(y, x)
    if y != H-1 and s[y+1][x] == ".":
        s[y + 1][x] = "*"
        y += 1
        addJinti(y, x)


H,W=[int(i) for i in input().split()]
sx=0
sy=0
s=[]
grids = []
for i in range(H):
    line = list(input())
    for j in range(W):
        if line[j] == '*':
            sy = i
            sx = j
    s.append(line)        

s[sy][sx] = '*'
addJinti(sy,sx)

for i in s:
    print("".join(i))



