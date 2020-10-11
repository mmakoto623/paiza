#STEP: 2 盤面の情報変更
H,W,N = [int(i) for i in input().split()]
S = [input() for i in range(H)]
for i in range(N):
	y,x = [int(i) for i in input().split()]
	tmp = list(S[y])
	tmp[x]  = '#'
	S[y] = "".join(tmp)

for i in range(H):
	print(S[i])