def print_argument(*args):
    for value in args:
        if type(value) == int:
            continue
        print(value)
print_argument(2,3.4,'s',1.0)

