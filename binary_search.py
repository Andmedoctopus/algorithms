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
	return None


def make_list(max):
	return list(range(1, max))

list1 = make_list(10)
list2 = make_list(15)
print(list2)
list2[4] = 4.5
print(list2)
print(binary_search(list1, 3))
print(binary_search(list2, 5))
