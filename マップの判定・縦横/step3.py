#STEP: 3 マップの判定・横
H,W = [int(i) for i in input().split()]
for i in range(H):
	line = input()
	for j in range(0,W):
		flg=False
		if j == 0:
			if line[1] =='#':
				flg=True
		elif j == (W-1):
			if line[W-2] =='#':
				flg=True
		elif line[j-1]=='#' and line[j+1]=='#':
			flg=True
		
		if flg == True:
			print(i,j)