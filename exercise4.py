from functools import reduce

# 1 Capitalize all of the pet names and print the list


def capitalize(li):
    return li.upper()


my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalize, my_pets)))
print(my_pets)  # it remains the same coz its a pure function :)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def fil(item):
    return item/100 > 0.5


print(list(filter(fil, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def combine(val1, val2):
    return val1+val2


print(reduce(combine, (my_numbers, scores)))
print(sum(my_numbers)+sum(scores))
