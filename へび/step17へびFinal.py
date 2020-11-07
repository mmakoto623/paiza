H,W,sy,sx,N = [int(i) for i in input().split()]
s = [list(input()) for i in range(H)]

#0:上 1:右 2:下 3:左
muki=0
RL={'R':1,'L':3,'X':0} #Xは向き変更なし

s[sy][sx] = '*'
old_t=0
old_d='X'
cnt=0 # 総移動カウンタ
for i in range(N+1):
    if i != N:
        t,d = input().split()
        t=int(t)

    muki = muki + RL[old_d]
    if muki >3:
        muki-=4

    flg = True
    for j in range(100):
        cnt+=1

        if muki == 0:
            sy-=1
        elif muki == 1:
            sx+=1
        elif muki == 2:
            sy+=1
        elif muki == 3:
            sx-=1
        if sy < 0 or sy > H-1 or sx < 0 or sx > W-1:
            flg = False
            break
        elif s[sy][sx] == '#':
            flg = False
            break
        elif s[sy][sx] == '*':
            flg = False
            break
        elif (cnt >= t and i != N) or cnt > 99:
            s[sy][sx] = '*'
            break
        else:
            s[sy][sx] = '*'

    if flg == False:
        break
    
    old_t = t
    old_d = d
    
for i in range(H):
    print("".join(s[i]))
    
