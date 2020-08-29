
def liner_search(numbers,key):
	for value in numbers:
		print(value)
		if key == value:
			return True
	else:
		return False
		

numbers = [100,200,30,40,5500]
key = 40

result = liner_search(numbers,key)
print("The all numbers is list :",numbers,type(numbers))
print(result)