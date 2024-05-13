list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
count = sum(1 for num in list1 if num in list2)
print(count)
