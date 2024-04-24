def greet(func):
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        return f"Good morning. {name}" + '\n'
    return wrapper
@greet
def Hello(name):
    return f"Hello {name}."

if __name__ == '__main__':
    result = Hello('Akshay')
    print(result)