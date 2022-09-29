a = 1


def change_value():
    a = 5
    print(a)


print(a)
change_value()  # it has is own memory soit wont interfere with the existing memory of variable a
print(a)
