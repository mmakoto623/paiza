#STEP: 11 移動が可能かの判定・方角
H,W,sy,sx,m = [i for i in input().split()]
H=int(H)
W=int(W)
sy=int(sy)
sx=int(sx)

s=[]
for i in range(0,H):
    s.append((input()))

if m == 'N':
    sy-=1
elif m == 'S':
    sy+=1
elif m == 'E':
    sx+=1
else:
    sx-=1

flg = True
if sy < 0 or sy >= H or sx < 0 or sx >= W:
    flg = False
else:
    if s[sy][sx] == '#':
        flg = False

if flg == True:
    print('Yes')
else:
    print('No')