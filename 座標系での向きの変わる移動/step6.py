#STEP: 6 マップからの座標取得
H,W = [int(i) for i in input().split()]

for i in range(0,H):
	line = input()
	for j in range(0,W):
	    if line[j] == '#':
	        print(i,j)

