def basic_fucntion(num1=0, num2=0, *other_numbers):
    '''
    This function prints the sum of provided numbers/integers.
    '''  # this will show the function description whil being called in an editor. I know, super cool!!!
    total = 0
    for num in other_numbers:
        total += other_numbers[0]
    sum = num1+num2+total
    print(sum)


basic_fucntion(2, 3, 5)
# also you can try help(basic_function) and basic_fucntion.__doc__
