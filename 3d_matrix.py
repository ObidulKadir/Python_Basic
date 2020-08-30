# 3-dimensional matrix

a = int(input("Enter the numbers of  rows :"))
b = int(input("Enter the numbers of column :"))

matrix =[]
for i in range(a):
	c=[]
	for j in range(b):
		j = int(input("Enter the value of matrix "+str(i)+" "+str(j)+":"))

		c.append(j) #value are converted into list.
	print()
	matrix.append(c)


for i in range(a):
	for j in range(b):
		print(matrix[i][j], end=" ")
	print('\n')