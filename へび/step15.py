#STEP: 15 幅のある移動

H,W,sy,sx,N = [int(i) for i in input().split()]
s = [list(input()) for i in range(H)]

muki = 0
RL={'R':1,'L':3}

s[sy][sx] = '*'
for i in range(1,N+1):
    d,l = input().split()
    l = int(l)
    houkou = muki + RL[d]
    if houkou > 3:
        houkou -=4

    flg = True
    for j in range(l):
        mx = sx
        my = sy
        if houkou == 0:
            my-=1
            muki=0
        elif houkou == 1:
            mx+=1
            muki = 1
        elif houkou == 2:
            my+=1
            muki = 2
        elif houkou == 3:
            mx-=1
            muki = 3
            
        if my < 0:
            my=0
            flg=False
            break
        elif my >= H:
            my=H-1
            flg=False
            break
        elif mx < 0:
            mx = 0
            flg=False
            break
        elif mx >= W:
            mx = W-1
            flg=False
            break
        elif  s[my][mx] == '#':
            flg = False
            break
        
        s[my][mx] = '*'
        sx = mx
        sy = my
        
    if flg == False:
        break
        
for i in s:
    print("".join(i))

