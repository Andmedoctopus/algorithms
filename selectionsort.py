import random

def findSmaller_index(arr):
	smallest = arr[0] 
	smallest_index = 0
	for i in range(1,len(arr)):
		if smallest > arr[i]:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectSort(arr):
	newarr = []
	for i in range(0, len(arr)):
		newarr.append(arr.pop(findSmaller_index(arr)))
	return newarr

our_arr = [3,4,2,1,5,3,2]
rand_arr = [random.randint(0,100) for i in range(0,10)]
print('our_arr = {}\nrand_arr = {}'.format(our_arr, rand_arr))
print('smallest in our_arr = {}\nsmallest in rand_arr = {}'.format(findSmaller_index(our_arr),findSmaller_index(rand_arr)))
print('sort our_arr = {}, \nsort rand_arr = {}'.format(selectSort(our_arr),selectSort(rand_arr)))