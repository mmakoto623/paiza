#STEP: 18 1 マスの陣取り
H,W =[int(i) for i in input().split()]

S=[]
x=0
y=0
for i in range(H):
    line = input()
    for j in range(W):
        if line[j] == '*':
            x = i
            y = j
    S.append(line)

for i in range(H):
    for j in range(W):
        if S[i][j] == '*':
            print('*',end="")
        elif (i == x-1 or i == x+1) and j == y:
            print('*',end="")
        elif (j == y-1 or j == y+1) and i == x:
            print('*',end="")
        else:
            print('.',end="")
    print("")
    
