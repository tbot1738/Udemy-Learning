def highest_even(list=[0]):
    highest_even_number = 0
    for item in list:
        if item % 2 == 0:
            if item > highest_even_number:
                highest_even_number = item
            else:
                pass
    print(highest_even_number)


highest_even([1, 3, 4, 5, 6, 8, 0])
