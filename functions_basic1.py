#1
def a():
    return 5
print(a())

prediction: 5 - correct


#2
def a():
    return 5
print(a()+a())

prediction below - correct
variable            value           console
a()                 5
a() + a()           10              10


#3
def a():
    return 5
    return 10
print(a())

prediction: 5 - correct


#4
def a():
    return 5
    print(10)
print(a())

prediction: 5 - correct


#5
def a():
    print(5)
x = a()
print(x)

prediction:
variable                value               console
a()                                         5
x                       a()                 undefined

Console shows 5 and NONE so prediction seems correct


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

prediction:
variable                value           console
a(b,c)                  print(b+c)
a(1,2)                  print(1+2)=print(3)
a(2,3)                  print(2+3)=print(5)
print(3) + print(5)                     3
                                        5

Console shows 3 and 5 on separate lines and an error message that + cannot be used for 'NoneType' and 'NoneType'. Once the print arguments are in the console, they are no longer numbers, but strings and the + operand cannot be used to add them.


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

prediction:
variable                value           console
str(b)                  '2'
str(c)                  '5'
                                        error                       

Console shows 25. It seems like numbers can be concatenated when using str().


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

prediction: - correct
variable                value           console
b                       100
                                        100
a()                     10              10


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

prediction: - correct
variable                value           console
a(2,3)              b = 2, c = 3        7
a(5,3)              b = 5, c = 3        14
a(2,3) + a(5,3)     7 + 14              21


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

prediction: - correct
variable                value           console
a(3,5)               b = 3, c = 5       8


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

prediction: - correct
variable                value           console
b                       500
                                        500
function
b                       300 
                                        500
function called                         
                                        300
                                        500


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

prediction: - correct
variable                value           console
b                       500
                                        500
                                        500
function is called
function
b                       300
                                        300
                                        300

                                        500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

prediction: - wrong
variable                value           console
b                       500
                                        500
                                        500
b                       a()
function runs                           300
                                        300

                                        300
                                        300

Console printed:
b = 500
>>> print(b)
500
>>> def a():
...     b = 300
...     print(b)
...     return b
...
>>> print(b)
500
>>> b=a()
300
>>> print(b)
300
>>>

Since the return value of the function was saved to a variable, it seems that the print statement in the function isn't printed in the console.


#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

prediction: - wrong
variable                value           console
                                        1
                                        b() undefined

Console printed:
>>> def a():
...     print(1)
...     b()
...     print(2)
...
>>> def b():
...     print(3)
...
>>> a()
1
3
2
>>>

I realized that a function can run another function even if it's defined outside of the original function.


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

prediction: - wrong
variable                value           console
y                       a()
function a()
x                       b()

function b()            5

a()                     x = 5           
y                       10
                                        10

Console prints:
>>> def a():
...     print(1)
...     x = b()
...     print(x)
...     return 10
...
>>> def b():
...     print(3)
...     return 5
...
>>> y = a()
1
3
5
>>> print(y)
10
>>>






































