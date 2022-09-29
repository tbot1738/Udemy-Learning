my_list = []


def appended():
    for char in 'hello':
        my_list.append(char)
    return my_list


print(appended())


# BETTER WAY

another_list = [char for char in 'hello']
list3 = [char ** 2 for char in range(0, 100, 2)]
other_list3 = [char ** 2 for char in range(0, 100) if char % 2 == 0]
print(another_list)
print(list3)
print(other_list3)
