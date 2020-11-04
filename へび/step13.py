#STEP: 13 移動が可能かの判定・複数回の移動
H,W,sy,sx,N = [int(i) for i in input().split()]

#0上1右2下3左
muki=0 #向いてい居る方向
RL={'R':1,'L':3}

s=[]
for i in range(0,H):
    s.append((input()))

for i in range(0,N):
    m = input()
    houkou = muki + RL[m]
    if houkou >3:
        houkou -=4
    
    if houkou == 0:
        sy-=1
        muki=0
    elif houkou ==1:
        sx+=1
        muki=1
    elif houkou ==2:
        sy+=1
        muki=2
    else:
        sx-=1
        muki=3
    
    if sy < 0 or sy > H-1 or sx < 0 or sx > W-1:
        print("Stop")
        break
    elif s[sy][sx] == '#':
        print("Stop")
        break
    else:
        print(sy,sx)