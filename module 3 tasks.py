'''
Objective
----------
1) d
2) a
3) 1
4) d
5) ????
6) <file_object>.read()
7) a
8) os.getcwd()
9) a
10) collection
11) d
12) a
13) a
14) a
15) c
16) d
17) d
18) lamda
19) b
20) *arg

Subjective
-----------
1
A function that is defined and implemented in one line and need not have a name when used with methods such as 'map()'

2
*args stores the arguements it recieves in a tuple but **kwargs stores it in a dictionary

3
Recursion is when a function is called within itself, leading to a loop of the same function within itself multiple times before unwrapping through each of them one by one

4
Local variables are only scoped to the specific function or class it is defined in, it cannot be used outside that particular function or class, where as global variables can be accessed from any where
in the code

5
import <module> # complete import
from <module> import <components. # specific import
from <module> import *  # * import

6
The location at which the module is stored in the case of python files, or in the python interpreter file in the case of other modules such as 'os' and 'sys'

7
randrange does not include the upper limit given and also includes a <step> parameter, both of which are not true for randint 

8
It is a collection of python files in a folder
To convert a folder to a package, add an empty '__init__'.py file in it

9
<file_object> = open('<file>', 'mode')

with open('<file>', '<mode>') as <file_object>:
    <operations>

10
<file_object>.tell() # get the current cursor postition
<file_object>.seek(<offset>, <whence>) # move the cursor to a specific position

'''
#Programming
#-----------
#1
def countinstring(string):
    lowercase = 0
    uppercase = 0

    for z in string:
        if z.islower():
            lowercase += 1
        elif z.isupper():
            uppercase += 1

    print('There are {} number of lower case letters'.format(lowercase))
    print('Thre are {} number of upper case letters'.format(uppercase))
    print()


string = input('Enter : ')
print()

countinstring(string)


#2
def checkforpalindrome(string):
    '''reversestring = ''

    for z in range(len(string) - 1, -1, -1):
        reversestring += string[z]'''

    if list(string) == list(string).reverse:
        print('The string is a palindrome')
    else:
        print('The string is not a palindrome')


string = input('Enter : ')
print()

checkforpalindrome(string)

#3
def operation(numbers):
    total = 0
    multiply = 1

    for z in numbers:
        z = int(z)
        total += z
        multiply *= z

    print('The total is {}'.format(total))
    print('The product is {}'.format(multiply))


numbers = input('Enter : ')
print()
numbers = numbers.split()

operation(numbers)

#4

def fibonacci(num1, num2):
    global counter, maxcounter

    num3 = num1 + num2
    print(num3)
    counter += 1

    if counter <= maxcounter:
        fibonacci(num2, num3)


counter = 0

maxcounter = int(input('How many numbers of the fibonacci series do you want? : '))
print()

if maxcounter < 2:
    print(0)
elif maxcounter == 2:
    print(0)
    print(1)
else:
    num1 = 0
    num2 = 1

    print(num1)
    print(num2)


    fibonacci(num1, num2)

#5

num = int(input('Enter a number : '))
print()

total = 0

for z in range(1, num + 1):
    if num % z == 0:
        total += z

print(total)

#6

num = input('Enter a number : ')
print()

total = 0

for z in num:
    total += int(z) ** 3

if str(total) == num:
    print('This number is an armstrong number')
else:
    print('This number is not an armstrong number')

#7
# the assumption has been made that the files for 'a' and 'b' are already created and have the integers in them before this code is run

a = open('a', 'r')
numa = int(a.read())
a.close()

b = open('b', 'r')
numb = int(b.read())
b.close()

c = open('c', 'w')

add = str(numa + numb)
sub = str(numa - numb)
mul = str(numa * numb)
div = str(numa / numb)

c.write(str(numa) + ' + ' + str(numb) + ' == ' + add + '\n')
c.write(str(numa) + ' - ' + str(numb) + ' == ' + sub + '\n')
c.write(str(numa) + ' * ' + str(numb) + ' == ' + mul + '\n')
c.write(str(numa) + ' / ' + str(numb) + ' == ' + div)


c.close()

