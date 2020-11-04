#STEP:10 座標系での向きの変わる移動
X,Y,N = [int(i) for i in input().split()]

#0上1右2下3左
muki=0
RL={'R':1,'L':3}
houkou = 0

for i in range(N):
    d = input()

    houkou = RL[d]+muki
    if houkou > 3:
	    houkou-=4

    if houkou == 0:
	    Y-=1
	    muki=0
    elif houkou == 1:
	    X+=1
	    muki=1
    elif houkou == 2:
	    Y+=1
	    muki=2
    else:
	    X-=1
	    muki=3
	    
    print(X,Y)
