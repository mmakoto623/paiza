#STEP: 9 座標系での規則的な移動
X,Y,N = [int(i) for i in input().split()]

#0上1右2下3左
muki={'N': 0, 'E': 1, 'S': 2, 'W': 3}
houkou = 1
idocnt=0 #２回移動するたびに向きが変わる
idoryo=1
nokori=N
for i in range(N):
	if nokori < idoryo:
		idoryo=nokori
	if houkou == 0:
		Y-=idoryo
	elif houkou == 1:
		X+=idoryo
	elif houkou == 2:
		Y+=idoryo
	else:
		X-=idoryo

	nokori-=idoryo
	if nokori<=0:
		break

	houkou+=1
	if houkou > 3:
		houkou-=4

	idocnt+=1
	if idocnt<2:
		idoryo=1
	elif idocnt==2:
		idoryo=2
	elif idocnt%2==0:
		idoryo+=1
	

print(X,Y)