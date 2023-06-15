from enum import Enum, unique, auto


# enumerations ---------------------------------------

@unique
class Fruit(Enum): 
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # MODI = 1 # this is error because we have @unique decorator, so values cannot be duplicated
    PEAR = auto()


# give objects number-like behavior
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0}, y:{1}>".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


# customize string representation of objects
class Person():
    def __init__(self):
        self.fname = 'Joe'
        self.lname = 'Baiden'
        self.age = 25

    def __repr__(self):
        return "<Person Class - fnmae:{0}, lname:{1}, age{2}>".format(self.fname, self.lname, self.age)

    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = "Person: {0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))


# special methods to compare objects
class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __eq__(self, other):
        return self.level == other.level


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    def __dir__(self):
        return ('rgbcolor', 'hexcolor')
        


def main():
    pass

    print(Fruit.APPLE)
    print(type(Fruit.APPLE)) # enum 'Fruit'
    print(repr(Fruit.APPLE)) # Fruit.APPLE: 1
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    print(Fruit.PEAR.value)

    myFruits = {}
    myFruits[Fruit.BANANA] = 'Come Mr.' # enums are hashable - can be used as keys
    print(myFruits[Fruit.BANANA])

    # object number-like operations
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    p3 = p1 + p2
    print(p3)

    p4 = p2 - p1
    print(p4)

    p1 += p2
    print(p1)

    # string representation
    cls1 = Person()

    print(repr(cls1))
    print(str(cls1))
    print('Formatted: {}'.format(cls1))
    print(bytes(cls1))

    # compare objects
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    print(Employee('Tim', 'Sims', 5, 9), Employee('John', 'Doe', 4, 12))
    print(bool(dept[0] > dept[2])) # who's senior?
    print(bool(dept[4] > dept[3])) # who's senior?

    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)

    # customize string representation of objects
    cls2 = myColor()
    print(cls2.rgbcolor)
    print(cls2.hexcolor) # print values of a computed attribute

    cls2.rgbcolor = (125, 200, 86) # set values of a computed attribute
    print(cls2.rgbcolor)
    print(cls2.hexcolor) 

    print(cls2.red) # access a regular attribute

    print(dir(cls2)) # list available attributes





if __name__ == '__main__':
    main()
