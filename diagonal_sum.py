# 3-dimensional matrix

n = int(input("Enter the numbers of n*n matrix :"))


matrix =[]
for i in range(n):
	c=[]
	for j in range(n):
		j = int(input("Enter the value of matrix "+str(i)+" "+str(j)+":"))

		c.append(j) #value are converted into list.
	print()
	matrix.append(c)


for i in range(n):
	for j in range(n):
		print(matrix[i][j], end=" ")
	print('\n')

#primary_diagonal_sumation
primary_diagonal = 0
secondary_diagonal = 0
for i in range(n):
	for j in range(n):
		if i == j:
			primary_diagonal = primary_diagonal + matrix[i][j]
		if(i+j==n-1):
			secondary_diagonal = secondary_diagonal + matrix[i][j]

print("Left diagonal Sum:",primary_diagonal)
print("Right diagonal Sum:",secondary_diagonal)