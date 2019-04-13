def binary_search(list, number):
	low  = 0
	high = len(list) - 1
	while low <= high:
		mid = (high + low) // 2
		if list[mid] == number:
			return mid
		elif list[mid] > number:
			high = mid - 1
		elif list[mid] < number:
			low = mid + 1
	return -1


def make_list(list, max):
	for i in range(1,max+1):
		list.append(i)
	return list

list1 = []
list2 = []
list1 = make_list(list1, 10)
list2 = make_list(list2, 15)
print(list2)
list2[4] = 4.5
print(list2)
print(binary_search(list1, 3))
print(binary_search(list2, 5))
