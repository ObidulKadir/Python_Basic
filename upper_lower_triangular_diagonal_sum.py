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
	print(end="  ")



print("Lower Triangular is")
for i in range(n):
	for j in range(n):
		if i>j:
			print(m[i][j], end=' ')

	print('\n')

print("Upper Diagonal Sum is :")
UpperDiagonalSum = 0
for i in range(n):
	for j in range(n):
		if i<j:
			if(i-j==2-n):
				UpperDiagonalSum=UpperDiagonalSum+m[i][j]

print(UpperDiagonalSum)

print("Lower Diagonal Sum is :")
LowerDiagonalSum = 0
for i in range(n):
	for j in range(n):
		if i>j:
			if(i-j==n-2):
				LowerDiagonalSum=LowerDiagonalSum+m[i][j]

print(LowerDiagonalSum)

