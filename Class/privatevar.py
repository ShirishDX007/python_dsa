class ClassSchedule:
    def __init__(self, course, instructor ):
        self.__course = course
        self.__instructor = instructor

    def display_course(self):
        print(f'Course: {self.__course}, Instructor: {self.__instructor}')
        
sched = ClassSchedule('Survey', 'Prof. Murthy')
#sched.__course

sched.display_course()



    
          
        
