def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')



def remind_name():
    print('Please, remind me your name.')
    name = input()
    if name == '' or name == ' ':
        print('What a strange name!')
        return remind_name()
    else:
        print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    res = int(input())
    while res != 2:
        print("Please, try again.")
        res = int(input())

def test_2():
    print("why do we use classes?")
    print("1. To group similar objects.")
    print("2. To give a class a common look and behavior.")
    print("3. To separate code and data.")
    res = int(input())
    while res != 2:
        print("Please, try again.")
        res = int(input())

def test_3():
    print("What is the output of the following code?")
    print("""
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)
""")
    res = int(input())
    while res != 3:
        print("Please, try again.")
        res = int(input())

    print('Completed, have a nice day!')

def test_4():
    print("A list can contain __________elements.")
    print("1. Unlimited(depending on the computer)")
    print("2. 1000")
    print("3. million")
    print("4.10 million")
    res = int(input())
    while res != 1:
        print("Please, try again.")
        res = int(input())

def end():
    input('Press y to restart or any other key to exit.')
    if input() == 'y':
        return greet('Bot', '2020')
    else:
        print('Congratulations, have a nice day!')



greet('K-218', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
test_2()
test_3()
test_4()
end()

