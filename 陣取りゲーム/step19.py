#STEP: 19 1マスの陣取り2
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
        elif S[i][j] == '#':
            print('#',end="")
        elif (i == x-1 or i == x+1) and j == y and S[i][j] == '.':
            print('*',end="")
        elif (j == y-1 or j == y+1) and i == x and S[i][j] == '.':
            print('*',end="")
        else:
            print('.',end="")
    print("")
