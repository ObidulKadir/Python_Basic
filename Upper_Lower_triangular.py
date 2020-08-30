#3*3 dimensional matrix

n = 3
m=[]
for i in range(n):
	c = []
	for j in range(n):
		j = int(input("Enter the values of matrix ["+str(i)+" "+str(j)+"] :"))
		c.append(j)
	print()
	m.append(c)


print("The matrix are: ...")
for i in range(n):
	for j in range(n):
		print(m[i][j],end=" ")
	print('\n')

print("Upper Triangular is")
for i in range(n):
	for j in range(n):
		if i<j:
			print(m[i][j], end=' ')

	print('\n')



print("Lower Triangular.is")
for i in range(n):
	for j in range(n):
		if i>j:
			print(m[i][j], end=' ')

	print('\n')

print("Upper Triangular sum is :")
Uppersum = 0
for i in range(n):
	for j in range(n):
		if i<j:
			Uppersum = Uppersum + m[i][j]

print(Uppersum)


print("Upper Triangular sum is :")
Lowersum = 0
for i in range(n):
	for j in range(n):
		if i>j:
			Lowersum = Lowersum + m[i][j]

print(Lowersum)

