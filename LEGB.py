#LEGB L-Local , E-Enclosed, G- Global, B- Builtin modules
from math import pi

#pi = "Outer Global variable"

def outer_pi():
    pi = "Outer pi variable"
    print(pi)

    def inner_pi():
        pi = "This is inner pi variable."
        print(pi) 
    inner_pi()
    
outer_pi()
print(pi)


