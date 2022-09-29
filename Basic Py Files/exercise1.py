# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Malina", 23)
cat2 = Cat("Adri", 12)
cat3 = Cat("Tbot", 18)

oldest_cat = ""
# 2 Create a function that finds the oldest cat


def oldest(*args):
    return max(args)


print(f"The oldest cat is {oldest(cat1.age,cat2.age,cat3.age)} years old.")
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
