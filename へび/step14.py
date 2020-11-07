#STEP: 14 移動が可能かの判定・幅のある移動
H,W,sy,sx,N = [int(i) for i in input().split()]
s = [input() for i in range(0,H)]
#0:上 1:右 2:下 3:左
muki = 0
RL={'R':1,'L':3}

for i in range(0,N):
    d,l = input().split()
    l=int(l)
    muki = muki + RL[d]
    if muki > 3:
        muki -=4
    
    flg = True
    for j in range(l):
        mx = sx
        my = sy
        if muki == 0:
            my-=1
        elif muki == 1:
            mx+=1
        elif muki == 2:
            my+=1
        elif muki == 3:
            mx-=1
            
        if my < 0:
            sy=0
            flg=False
            break
        elif my >= H:
            sy=H-1
            flg=False
            break
        elif mx < 0:
            sx = 0
            flg=False
            break
        elif mx >= W:
            sx = W-1
            flg=False
            break
        if  s[my][mx] == '#':
            flg = False
            break
        
        sx = mx
        sy = my
    
    print(sy,sx)

    if flg == False:
        print("Stop")
        break
