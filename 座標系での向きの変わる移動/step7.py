#STEP: 7 座標系での移動・方角
Y,X,N  = [int(i) for i in input().split()]
for i in range(N):
	d = input()
	if d == 'N':
		Y-=1
	elif d == 'S':
		Y+=1
	elif d == 'W':
		X-=1
	elif d == 'E':
		X+=1
	print(Y,X)