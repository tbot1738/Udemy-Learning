# walrus operator can assign a variable to a statement or code of lne in between the function

# Denoted by :=

# without walrus

a = "Helo UwU oni chan"
n = len(a)

if (n > 10):
    print("Character limit exceeded")

# with walrus
a = "Helo UwU oni chan"

if((n := len(a)) > 10):
    print("Character limit exceeded")

# another example
while (n > 10):
    print(a)
    a = a[:-1]
    n = len(a)
