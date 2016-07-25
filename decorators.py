from logging import getLogger

log = getLogger(__name__)

def decorator_exercise(func):
    def function_wr(*args, **kwargs):
        return "<h1>{}<h1>".format(func(*args, **kwargs))
    return function_wr

class Person:
    def __init__ (self):
        self.name = "Ben"
        self.second_name = "Scott"

    @decorator_exercise
    def get_name (self):
        return self.name + " " + self.second_name

new_person = Person()

print (new_person.get_name())
