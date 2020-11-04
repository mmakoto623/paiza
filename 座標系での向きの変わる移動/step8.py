#STEP: 8
Y,X,D = [i for i in input().split()]
Y=int(Y)
X=int(X)
d = input()
#0上1右2下3左
muki={'N': 0, 'E': 1, 'S': 2, 'W': 3}
RL={'R':1,'L':3}

houkou = RL[d]+muki[D]
if houkou > 3:
	houkou-=4

if houkou == 0:
	Y-=1
elif houkou == 1:
	X+=1
elif houkou == 2:
	Y+=1
else:
	X-=1
print(Y,X)