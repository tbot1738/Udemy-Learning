from multiprocessing.reduction import duplicate


list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = []

for item in list:
    if list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)
