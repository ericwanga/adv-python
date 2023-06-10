# some advanced python functions
# 2023-06-09

from pathlib import Path
from string import Template
import itertools
import collections
import pandas as pd


# list of all tables used in the original database
TABLES = [
    "addresses",
    "birthdates",
    "cities",
    "countries",
    "cuisines",
    "districts",
    "food",
    "orders",
    "promos",
    "restaurants",
    "states",
    "users",
]

# structure holding initial database
MultiDimDatabase = collections.namedtuple("MultiDimDatabase", TABLES)
ReducedDatabase = collections.namedtuple("ReducedDatabase", ["orders", "users", "food", "promos", "restaurants", "addresses"])

# prepare functions
def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2
        
def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"

def predFunction(x):
    return x < 40

def myDocStringFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> nothing to do

    Parameters:
    arg1: first argument
    arg2: second argument, defaults to None
    """
    print(arg1, arg2)

def addition(*args):
        result = 0
        for arg in args:
            result += arg
        return result

def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32

def FahrenheitToCelsisus(temp):
    return (temp - 32) * 5/9

# --- Task # 2 ---
def reduce_dims(db: MultiDimDatabase) -> ReducedDatabase:
    # # raise NotImplementedError()
    # try:
    #     red_db_orders = db.orders
    #     red_db_users = pd.merge(db.users, db.birthdates, left_on='birthdate_id', right_index=True)
    #     red_db_food = db.food.merge(db.cuisines, on='cuisine_id')
    #     red_db_promos = db.promos
    #     red_db_restaurants = db.restaurants
    #     red_db_addresses = db.addresses.merge(db.districts,on='district_id').merge(db.cities,on='city_id').merge(db.states,on='state_id', suffixes=('_city', '_state')).merge(db.countries,on='country_id', suffixes=('_state', '_country'))
    # except Exception as e:
    #     print('ERROR:', e)

    try:
        ReducedDatabase.orders = db.orders
        ReducedDatabase.users = pd.merge(db.users, db.birthdates, left_on='birthdate_id', right_index=True, how='left')
        ReducedDatabase.food = db.food.merge(db.cuisines, left_on='cuisine_id', right_index=True, how='left')
        ReducedDatabase.promos = db.promos
        ReducedDatabase.restaurants = db.restaurants
        ReducedDatabase.addresses = pd.merge(db.addresses, db.districts, left_on='district_id', right_index=True, how='left').\
            merge(db.cities, left_on='city_id', right_index=True, suffixes=('_district', '_city'), how='left').\
            merge(db.states, left_on='state_id', right_index=True, suffixes=('_city', '_state'), how='left').\
            merge(db.countries, left_on='country_id', right_index=True, suffixes=('_state', '_country'), how='left')
    except Exception as e:
        print('ERROR:', e)
    
    # return collections.namedtuple('ReducedDatabase', [red_db_orders, red_db_users, red_db_food, red_db_promos, red_db_restaurants, red_db_addresses])
    return ReducedDatabase


def main():

    # string functions ---------------------------------------
    # data
    byt = bytes([0x41, 0x42, 0x43, 0x44])
    st = 'This is a string'

    # encode, decode
    st2 = byt.decode('utf-8')
    print(st+st2) # This is a stringABCD

    byt2 = st.encode('utf-8')
    print(byt+byt2) # b'ABCDThis is a string'

    byt3 = st.encode('utf-32')
    print(byt3) # b'\xff\xfe\x00\x00T\x00\x00\x00h\x00\x00\ ......'


    # template
    # create a template
    temp1 = Template('You are watching ${function} in ${IDE}')
    # use substitute
    str2 = temp1.substitute(function="'Template' from 'string'", IDE='VScode') # with keyword arguments
    print(str2)

    # use substitute
    data = {'function': '"Template" from "string"', 'IDE': 'VScode'} # with a dictionary
    str3 = temp1.substitute(data)
    print(str3)


    # python built-in utilities -----------------------------
    # data
    list1 = [1,2,3,0,5,6] 
    
    # any
    print(any(list1)) # return any values are true

    # all 
    print(all(list1)) # return true if all values are true

    # min, max, sum
    print(min(list1))
    print(max(list1))
    print(sum(list1))


    # iterators --------------------------------------
    # data
    days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    daysFrench = ['Dim','Lun','Mar','Mer','Jeu','Ven']
    
    # iter 
    i = iter(days) # over a collection
    print(next(i))
    print(next(i))
    print(next(i))

    # iter 
    with open('02 Builtin Functions/testfile.txt', 'r') as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # range
    for m in range(len(days)):
        print(m, days[m])
    
    # enumerate 
    for i, m in enumerate(days, start=1):
        print(i, m)

    # zip
    for m in zip(days, daysFrench):
        print(m)

    # zip to combine sequence
    for i, m in enumerate(zip(days, daysFrench), start=1):
        print(i, m[0], '=', m[1], 'in French')


    # transforms -------------------------------------
    # data
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # fitler    
    odds = list(filter(filterFunc, nums)) # remove items from a list
    print(odds)
    
    # filter
    lowers = list(filter(filterFunc2, chars)) # on non-numeric sequence
    print(lowers)

    # map
    squares = list(map(squareFunc, nums)) # create a new sequence
    print(squares)

    # map (with sort)
    grades = sorted(grades)
    letters = list(map(toGrade, grades)) # change (map) numbers to grades
    print(letters)


    # itertools ---------------------------
    # data
    seq1 = ['a','b','c','d','e']
    vals = [10,20,30,40,50,40,30]
    
    # cycle
    cycle1 = itertools.cycle(seq1) # over a collection
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # count
    count1 = itertools.count(100, step=10) # to create counter
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate
    accu = itertools.accumulate(vals) # to accumulate values
    accumax = itertools.accumulate(vals, max)
    print(list(accu))
    print(list(accumax))

    # chain
    x = itertools.chain(seq1, vals, 'XYZ') # connect sequences together - note: "XYZ" will be split
    print(list(x)) # ['a', 'b', 'c', 'd', 'e', 10, 20, 30, 40, 50, 40, 30, 'X', 'Y', 'Z']

    # dropwhile, takewhile
    print(list(itertools.dropwhile(predFunction, vals))) # drop values when the function condition is met
    print(list(itertools.takewhile(predFunction, vals))) # keep values when the function condition is met


    # advanced functions ----------------------------------
    # docstring
    # those "description" strings are stored in __doc__
    print(myDocStringFunction.__doc__)
    # print(itertools.__doc__)
    print(Path.__doc__)

    # variable arguments
    # refer to above function definition
    print(addition(5, 10, 15, 20)) # pass different arguments

    myNums = [5, 10, 15, 20]
    print(addition(*myNums)) # pass a list

    # keyargs
    # when keyword arg is used in function definition, must use the keyword when invoking the function
    # i.e., must use keyword when it is there

    # lambda
    # data
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # use regular function
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # use lambda
    print(list(map(lambda t: (t - 32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))

    
    # collections --------------------------------------
    # basic collections
    # list, tuple, set, dictionary

    # advanced collections
    # namedtuple                   Tuple with named fields
    # OrderedDict, defaultdict     Dictionaries with special properties
    # Counter                      Counts distinct values
    # deque                        Double-ended list object

    # namedtuple!!
    # example 1
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    
    print(p1, p2)
    print(p1.x, p1.y)

    p1 = p1._replace(x=100)
    print(p1)
    
    # example 2
    tables = [pd.read_csv(Path('tables/' + t + '.csv'), index_col=0) for t in TABLES]

    # db1 = MultiDimDatabase(tables[0], tables[1], tables[2], tables[3], tables[4], tables[5])
    db1 = MultiDimDatabase(*tables)
    print(db1.addresses)
    print(db1.cities)
    print(db1.countries)
    print(db1.states)
    print(db1.users)
    print(db1.birthdates)
    # print(db1.users.info())

    db2 = reduce_dims(db1)
    print(db2.users)
    print(db2.food)
    print(db2.addresses)











if __name__ == '__main__':
    main()
    print(f'__file__: {__file__}')
    print(f'Path(__file__): {Path(__file__)}')
