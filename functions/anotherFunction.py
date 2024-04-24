def another_function(func):
    """This function accepts another function."""

    def other_function():
        val = "this function returns %s of %s" % (func(), eval(func()))
        return val

    return other_function


def a_function():
    """This is a useless function."""
    return 2+2

if __name__ == '__main__':
    value = a_function()
    decorator = another_function(a_function)
    print(value)
