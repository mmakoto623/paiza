#STEP: 12 移動が可能かの判定・方向
H,W,sy,sx,d,m = [i for i in input().split()]
H=int(H)
W=int(W)
sy=int(sy)
sx=int(sx)

muki={'N':0,'E':1,'S':2,'W':3}
houkou={'R':1,'L':3}

s=[]
for i in range(0,H):
    s.append((input()))
    
susumu = muki[d]+houkou[m]
if susumu > 3:
    susumu-=4
if susumu == 0:
    sy-=1
elif susumu == 1:
    sx+=1
elif susumu == 2:
    sy+=1
else:
    sx-=1

if sy < 0 or sy > H-1 or sx < 0 or sx > W-1:
    print("No")
elif s[sy][sx] == '#':
    print("No")
else:
    print("Yes")

