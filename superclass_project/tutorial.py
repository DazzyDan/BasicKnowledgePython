from setuptools import SetuptoolsDeprecationWarning


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def output_name(self, firstname, lastname):
        full_name = f"{lastname} {firstname}"
        return full_name


class Student(Person):
    def __init__(self, firstname, lastname, birthday):
        '''
            Python also has a super() function that will make the child class 
            inherit all the methods and properties from its parent:
        '''
        super().__init__(firstname, lastname)
        self.birthday = birthday
    def welcome(self, s_l, s_f):
        message = f"Welcome {self.output_name(s_f,s_l)} born in {self.birthday}"
        return message

class Teacher(Student):
    # Student here has already inherit Person class, so don't need inherit twice
    def __init__(self, firstname, lastname, birthday, class_name,t_f, t_l):
        super().__init__(firstname, lastname, birthday)
        self.class_name = class_name
        self.teacher_f = t_f
        self.teacher_l = t_l
    
    def assign_class(self):
        teacher_fullname = self.output_name(self.teacher_f, self.teacher_l)
        print(f"{self.welcome(self.firstname, self.lastname)} will study in class {self.class_name} under the teach of {teacher_fullname}")
    
class NewStudent(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    def get_acronym(self):
        acronym = self.lastname[0] + self.firstname[0]
        return acronym
class NewClass(NewStudent):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    def assign_new_class(self):
        a = self.get_acronym() + " Class1"
        print(a)
    
# p = Person("Dazzy", "WANG")
t = Teacher("Eloise", "HU", "1999/09/09", "Class2", "Doge", "Woof")
t.assign_class()
# if here use NewStudent , it cannot get assign_new_class function 
# because NewStudent doesn't inherit from NewClass
# We can choose the last level in the inheritance tree, which can get all the functions
n = NewClass("Dazzy", "WANG")
n.assign_new_class()
print(n.get_acronym())
    
    