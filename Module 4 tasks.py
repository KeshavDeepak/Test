# programming

#1
class StringThatCanBeReversed:
    def __init__(self, string):
        self.value = string

    def reverse(self):
        listofwords = self.value.split()
        listofwords.reverse()
        self.value = ''

        for z in listofwords:
            self.value += (z + ' ')

    def print(self):
        print(string1.value)


string1 = StringThatCanBeReversed('python is an easy language')
string1.reverse()
string1.print()


#2
from math import pi


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def printarea(self):
        print('The area is ' + str(self.radius ** 2) + 'π')

    def printperimeter(self):
        print('The perimeter is ' + str(self.radius * 2) + 'π')


circle1 = Circle(4)
circle1.printarea()
circle1.printperimeter()

#3
file = open('demo.txt', 'r')

for z in file.readlines():
    split = z.split()
    
    if len(split) == 3:
        if split[0] == '+91' and len(split[0]) == 3 and len(split[1]) == 5 and len(split[2]) == 5:
            if split[0][1:].isdigit() and split[1].isdigit() and split[2].isdigit():
                print(z)

file.close()

#4
numberofemails = int(input('Enter the number of emails you want to give  : '))

dict = {}

for z in range(numberofemails):
    email = input('Enter email : ')

    if email.split('@')[1] in dict.keys():
        currentvalue = dict[email.split('@')[1]]
        dict[email.split('@')[1]] = currentvalue + ', ' + email.split('@')[0]
    else:
        dict[email.split('@')[1]] = email.split('@')[0]

print()
print(dict)

#5
class ValuesNotEqual(Exception):
    pass


num1 = int(input('Enter the first number : '))
num2 = int(input('Enter the second number : '))
print()

try:
    if num1 != num2:
        raise ValuesNotEqual
    else:
        print('The values are equal')
except ValuesNotEqual:
    print('The values are not equal')
