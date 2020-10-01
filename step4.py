#STEP: 4 マップの判定・縦
H,W = [int(i) for i in input().split()]
S = [input() for i in range(H)]
for y in range(0,H):
	for x in range(0,W):
		flg=False
		
		if y == 0:
			if S[1][x] =='#':
				flg=True
		elif y == (H-1):
			if S[H-2][x] =='#':
				flg=True
		elif S[y-1][x] =='#' and S[y+1][x]=='#':
			flg=True
		
		if flg == True:
			print(y,x)