#STEP: 1 盤面の情報取得
H,W,N = [int(i) for i in input().split()]
S = list([input() for i in range(H)])
for i in range(N):
    y,x = [int(i) for i in input().split()]
    print(S[y][x])
