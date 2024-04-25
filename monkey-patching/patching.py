import module

def monkey_f(self):
    print("monkey_f is being called")

#replacing address of func with monkey_f
module.A.func = monkey_f
obj = module.A()

obj.func()