ar_input = int(input('Enter the range :'))

l = []
print("Enter the Value : ")
for i in range(ar_input):
	j = int(input())
	l.append(j)
print(l)

x  = max(l)
print(x)
maxCount = l.count(x)
print(maxCount)