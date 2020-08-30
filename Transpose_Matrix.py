# 3-dimensional matrix and tranpose matrix

n = int(input("Enter the numbers of n*n matrix :"))


matrix =[]
for i in range(n):
	c=[]
	for j in range(n):
		j = int(input("Enter the value of matrix ["+str(i)+" "+str(j)+"]:"))

		c.append(j) #value are converted into list.
	print()
	matrix.append(c)

print("The matrix is :")
for i in range(n):
	for j in range(n):
		print(matrix[i][j], end=" ")
	print('\n')


t = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
	for j in range(n):
		t[i][j] = matrix[j][i]#just swap the values

print("The Transpose Matrix is :")
for i in range(n):
	for j in range(n):
		print(t[i][j], end=" ")
	print('\n')

