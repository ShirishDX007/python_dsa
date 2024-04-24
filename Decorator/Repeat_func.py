from  functools import wraps
import time

def repeat_something(times):
    """ This is parameterized type decorator which accepts argument."""
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                    result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate
@repeat_something(3)
def Greetings(msg):
    '''Greet when someone arrives at
    reception area.'''
    print(msg)

def question(ask):
    time.sleep(3)
    print(ask)

help(repeat_something)
Greetings("Hello!, Good Morning.")
question("how may I help you?")

