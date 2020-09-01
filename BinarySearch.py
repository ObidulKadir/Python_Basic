#Binary search 
pos = 0
def Binary_Search(list,key):
	l = 0  #lower bound index
	u = len(list) - 1 #upper bound index

	while l <= u :
		mid = (l+u) // 2

		if list[mid] == key:
			globals()['pos'] = mid
			return True
		else:
			if list[mid] < key :
				l = mid + 1
			else:
				l = mid - 1
	else:
		return False

list = [3,4,5,6,9,10]
key  = 10
if Binary_Search(list,key):
	print("Item is found at ",pos)
else:
	print("Not found")
