import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in time {end_time - start_time} seconds.")
        return result
    return wrapper

class Myclass:
    @timing
    def my_method(self):
        time.sleep(3)
        return print("some task was going on..")

object = Myclass()
object.my_method()