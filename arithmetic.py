def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(*args):
    total = args[0]
    for num in args[1:]:
        total -= num
    return total

def multiply(*args):
    total = args[0]
    for num in args[1:]:
        total *= num
    return total

def divide(*args):
    total = args[0]
    for num in args[1:]:
        total /= num
    return total

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 ** 3

def power(*args):
    total = args[0]
    for num in args[1:]:
        total **= num
    return total

def mod(*args):
    total = args[0]
    for num in args[1:]:
        total %= num
    return total
