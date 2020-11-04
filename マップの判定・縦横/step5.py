#FINAL問題 マップの判定・縦横
H,W = [int(i) for i in input().split()]
S = [input() for i in range(H)]

def tate(y,x):
    tmp=""
    if y == 0:
        tmp+=S[1][x]
    elif y == H-1:
        tmp+=S[H-2][x]
    else:
        tmp+=S[y-1][x]+S[y+1][x]
    return tmp

def yoko(y,x):
    tmp=""
    if x == 0:
        tmp+=S[y][1]
    elif x == W-1:
        tmp+=S[y][W-2]
    else:
        tmp+=S[y][x-1]+S[y][x+1]
        
    return tmp
    
for y in range(0,H):
  for x in range(0,W):
    tmp = ""
    tmp = tate(y,x)
    tmp += yoko(y,x)
    if tmp.count('.') == 0:
      print(y,x)
      
