#STEP23:陣取りゲーム
H,W = [int(i) for i in input().split()]
N = input()

s=[]
ax=0
ay=0
bx=0
by=0
ban = N

for i in range(H):
    line = input()
    for j in range(W):
        if line[j] == 'A':
            ax = j
            ay = i
        elif line[j] == 'B':
            bx = j
            by = i
    s.append(list(line))

def addJinti(y,x,ban):
    jin=[]
    if x != 0 and s[y][x-1] == ".":
        s[y][x - 1] = str(ban)
        jin.append([y,x-1])
    if x != W-1 and s[y][x + 1] == ".":
        s[y][x + 1] = str(ban)
        jin.append([y,x+1])
    if y != 0 and s[y-1][x] == ".":
        s[y - 1][x] = str(ban)
        jin.append([y-1,x])
    if y != H-1 and s[y+1][x] == ".":
        s[y + 1][x] = str(ban)
        jin.append([y+1,x])
    return jin


ajin = []
ajin.append([ay,ax])
bjin = []
bjin.append([by,bx])
acnt=1
bcnt=1
old = 0
old2= 0
while True:
    if ban == 'A':
        j=[]
        j2 =[]
        for i in ajin:
            res=[]
            ay,ax = i
            res = addJinti(ay,ax,ban)
            if len(res) > 0:
                j+=res
                acnt+=len(res)
            else:
                #陣地を増やせなかった陣地を保存
                j2.append([ay,ax])

        ajin+=j
        for i in j2:
            ajin.remove(i)
        
        ban = 'B'
    elif ban == 'B':
        j=[]
        j2=[]
        for i in bjin:
            res=[]
            by,bx = i
            res = addJinti(by,bx,ban)
            if len(res) > 0:
                j+=res
                bcnt+=len(res)
            else:
                #陣地を増やせなかった陣地を保存
                j2.append([by,bx])

        bjin+=j
        for i in j2:
            bjin.remove(i)
        ban = 'A'
        
    if (acnt+bcnt) == H*W or ((acnt+bcnt) == old and old2== old):
        break
    old2 = old
    old = acnt+bcnt
    

print(acnt,bcnt)

if acnt>bcnt:
    print("A")
else:
    print("B")
