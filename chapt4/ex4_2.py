import math


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")


repeat_lyrics()
# Exercise 2 had me put the call at before the function was defined.
# This caussed an error

# Exercise 3 had me move print_lyrics after repeat. the code still worked

# Function definitions do not alter the flow of execution


def print_twice(bruce):  # bruce is the parameter
    print(bruce)
    print(bruce)


print_twice(math.pi)  # math.pi is the argument


def add_two(a, b):
    added = a + b
    return added


x = add_two(3, 5)
print(x)

# ex 4:
# def keyword indicates start of a function and the following indented code
# is to be stored for later
# ex 5: answer is D


def fred():
    print("Zap")


def jane():
    print("ABC")


jane()
fred()
jane()


def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"


print(greet('fr'), "Luna")
