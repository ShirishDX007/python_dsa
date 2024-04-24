def many_args(*args, **kwargs):
    print(args)
    print(kwargs)

many_args(2024, 12, 23, name = 'Brad pitt')