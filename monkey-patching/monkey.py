#monkey patching is a technique to modify behaviour of class, function or module

def add_speech(cls):
    cls.speak = lambda self, message: print(message)
    return cls
    
@add_speech
class Robot:
    def __init__(self, name):
        self.name = name

Robot = add_speech(Robot)

robot = Robot('optimus prime')
robot.speak(f'Hi, I am {robot.name} ')