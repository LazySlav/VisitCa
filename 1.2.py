a = [int(i) for i in input().split()]
s = []
for j in range(len(a)):
	max = 0
	temp = 0
	for i in a:
		if (i>max):
			max = i
	a.remove(max)
	s.append(max)
print(s)
