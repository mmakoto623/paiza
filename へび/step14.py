#STEP: 14 移動が可能かの判定・幅のある移動
H,W,sy,sx,N = [int(i) for i in input().split()]
s = [input() for i in range(0,H)]

muki = 0
RL={'R':1,'L':3}

for i in range(0,N):
    d,l = input().split()
    l=int(l)
    houkou = muki + RL[d]
    if houkou > 3:
        houkou -=4
    
    flg = True
    for j in range(l):
        mx = sx
        my = sy
        if houkou == 0:
            my-=1
        elif houkou == 1:
            mx+=1
        elif houkou == 2:
            my+=1
        elif houkou == 3:
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
    muki = houkou
    if flg == False:
        print("Stop")
        break
