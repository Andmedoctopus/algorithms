def binary_search(list, number):
    low = 0
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


def make_list(border):
    return list(range(1, border))


list1 = make_list(10)
list2 = make_list(15)
print(list2)
list2[4] = 4.5
print(list2)
print(binary_search(list1, 3))
print(binary_search(list2, 5))


# Look at small magic
class ListWithBinarySearch(list):
    def binary_search(self, number):
        return binary_search(self, number)

    @classmethod
    def list_example(cls, range_border):
        return ListWithBinarySearch(range(1, range_border))


# And now you can write your code so)
print('Examples with new class')

# Create your own object of new class
new_list = ListWithBinarySearch([1, 2, 3, 4, 5, 6])
print(new_list.binary_search(4))
print(new_list.binary_search(7))

# Or can get random list using class method

random_list = ListWithBinarySearch.list_example(50)
print(random_list.binary_search(3))
print(random_list.binary_search(61))
