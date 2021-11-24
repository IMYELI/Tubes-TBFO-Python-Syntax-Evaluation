import datetime
x = datetime.datetime.now()
print(x)

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thislist = ["monkagiga", 123]
thistuple = ([1, 2], "haha")
