#STEP: 24 裏返せる可能性（縦横）
H,W,Y,X = [int(i) for i in input().split()]

for i in range(H):
    for j in range(W):
        if i == Y and j == X:
            print("!",end="")
        elif i==Y:
            print("*",end="")
        elif j==X:
            print("*",end="")
        else:
            print(".",end="")
    print("")
