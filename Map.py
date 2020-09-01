

"""
map(function,Iterable)

"""

def fn_name(i):
	return i**2


l = [10, 20, 30, 40]

result = map(fn_name, l) 
""" if we do this way we found a map object which is iterable object
or we can do another way 
result = list(map(fn_name,l))
we direct result here
"""
print(result)
for values in result:
	print(values)
	
""" after get map iterable object we have to print yhat result 
if we go into the loop function than we are able to get all values of list
 
 