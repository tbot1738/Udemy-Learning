def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**This decorator will now super boost the functions**")
        func(*args, **kwargs)
    return wrap_func


@my_decorator
def hello(some_random_arg="Hmm", emoticon="UwU"):
    print("Greetings!", some_random_arg, emoticon)


hello()
