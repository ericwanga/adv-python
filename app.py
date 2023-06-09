# my codes of advanced python coding for those I don't know
# as app structure + debugging, not in notebook cells
# 2023-06-09

from pathlib import Path

# filter functions
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
        

def main():

    list1 = [1,2,3,0,5,6]
    print(any(list1))

    # iterators
    # data
    days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    daysFrench = ['Dim','Lun','Mar','Mer','Jeu','Ven']
    
    # iter
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    with open('02 Builtin Functions/testfile.txt', 'r') as fp:
        for line in iter(fp.readline, ''):
            print(line)
    
    # enumerate
    for i, m in enumerate(days, start=1):
        print(i, m)

    # zip
    for i, m in enumerate(zip(days, daysFrench), start=1):
        print(i, m[0], '=', m[1], 'in French')

    # filter
    # data
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # fitler    
    odds = list(filter(filterFunc, nums))
    print(odds)
    
    # filter
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # map
    squares = list(map(squareFunc, nums))
    print(squares)

    # map
    



if __name__ == '__main__':
    main()
    print(f'__file__: {__file__}')
    print(f'Path(__file__): {Path(__file__)}')
