my_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = list(set([item for item in my_list if my_list.count(item) > 1]))

print(duplicates)
