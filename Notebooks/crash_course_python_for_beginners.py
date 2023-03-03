# -*- coding: utf-8 -*-
"""Crash Course Python for beginners.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oSOGlASZUE4Z7kIa0r_u5NiVwSgNsyaV

# Crash Course Python for beginners

To get you up to speed for AI Code, in this notebook we rapidly go over some essential aspects of coding and basics of Python programming. Follow the instructions in this notebook to get a grip of the fundamental concepts. At the end, there will be some exercises to test if you have mastered the basics. **Good luck!**
 
At the end of this notebook you will be able to:
-   Work with different types of data
-   Create and use variables
-   Create functions and implement existing functions
-   Use conditional statements and operators
-   Produce loops
-   Work with lists and dictionaries

## 0. Showing results & Commenting

First we will start with the basics of using a Jupyter Notebook (an .ipynb file) such as this one we're working on. These notebooks consist of cells that contain regular texts like this one or ones that contain expressions as code blocks, such as the one given below.
"""

print("Hello Jupyter!")

"""When you run an expression in a notebook (by selecting the code cell and pressing Ctrl+Enter or simply clicking the play button that appears on the left of the cell when you hover over it), the result of the expression is shown below it. Try it out!"""

7 + 2

5 - 1
6 + 10

"""Notice that python only displays the result of the last called expression. In order to show multiple results, you have to use the print() function.
 
"""

print(5 - 1)
print(6 + 10)

"""You'll notice later that as your code gets more complicated and as you collaborate on a single code with others, you often need explanations and notes within your code. It is also important that whatever note you take does not affect the execution of your code. 

For this, Python provides *comments*. You can write comments by putting a # at the beginning of the statement. Such statements won't be executed when you run the code.
"""

print("This text will be printed")
#print("This won't")

print("You can also comment next to statements to note something about that statement") # like this

"""However if your comment extends one line, you'll need to use multiline strings (which will be ignored by Python since they are not inside a print statement ) using `''' comment '''`"""

print("You can also comment next to statements to note something about that statement") # like this
but not like this

print("You can write multiple line comments") # this
# this

"""
Or 
like 
this
"""
print("You can write multiple line comments")

"""Awesome! Now that you now the basics of using the Jupyter Notebooks and Python for showing results and taking notes, you're already one step closer to becoming an AI engineer!

## 1. Different types of data

Now we will continue with learning the most essential concept of Python that allow us to play with different types of values such as numbers and texts that may be required to construct algorithms and programs. Such values are our data. There are many different types of data in Python. All with their own special attributes. To keep things clear we will start by introducing the 3 most basic types:
- Strings
- Integers
- Floats

### Strings

A string represents data in the form of texts. Strings consist of characters and is always enclosed with single or double quotes. Or for a string that expands onto multiple lines, you need three double or single quotes.
"""

print("Hello World")
print('Hello World')
print("""Hello
      World""")

"""Do you think the line given below will run smoothly?"""

print(Hello_World)

"""No! Without the quotes, Python will think that you are using a variable. If the variable is not defined you get an error, we will come back to this later in the notebook.

There are many other things you can do with strings, but we will cover them in the proceeding sections of this notebook.

### Integers

An integer is a whole number, positive or negative. So a number without decimals.
"""

print(1000000)
print(-100000)

"""When using large integers in python it is important to know that you can not use commas as separators to make it more readable, but underscores do work for that purpose."""

print(1_000_000)
print(1,000,000)

"""### Floats

Floats are numbers with decimals, again positive or negative. Every number that is followed with a "**.**" will be considered a float.
"""

print(3.3)
print(-3.3)

"""Make sure to always use a  .  as a decimal point. Commas in python are used for the separation of values."""

print(3,3)

"""### Data Types - Summary

There are other data types in Python that are often used. The ones explained in these sections are the atomic data types in Python. It is important to be aware of what is the type of your data and to be coherent in terms of types. In order to quickly check what type of data you are dealing with you can use the *type()* function

"""

type(13.)

type(13)

type("13")

"""### Changing types

Sometimes in order to fit your data into a certain algorithm, you will need to change the type of the data. This is possible with typecasting functions:
- str(): returns a string
- int(): returns an integer
- float(): returns a float
"""

print(10/3)
type(10/3)

print(int(10/3))
type(int(10/3))

print(str(10/3))
type(str(10/3))

"""### Basic calculations

Basic calculations combine two values with one operator in between them. Some straightforward operators are:

    +   addition
    -   subtraction
    *   multiplication
    /   division
    //  integer division
    **  power
    %   modulo
    
Here are some examples:
"""

print(14+5)
print(14-5)
print(14*5)
print(14/5)
print(14//5)
print(14**5)
print(14%5)

"""We will assume this does not need any more explanation. Only the integer division and modulo might be unfamiliar. 

The integer division (//) is simply a division that rounds down to a whole number. The modulo operator (%) takes the remainder of a division. In very simplistic terms: if we have 14 cookies which we have to divide over 5 children, each child gets 2 cookies. And we still have 4 cookies left. Thus, dividing 14 by 5 as an integer division is 2, while 14 modulo 5 is the remainder 4.

So far, so good. Now that you know about the different types of data we can continue to the next chapter

## 2. Variables

In order to handle the data values in our program systematically, we need flexible and stable structures. These are called variables in Python. To make a variable you are free to choose the names as you like them, provided that you follow a few simple rules, namely:

- A variable name must consist of only letters, digits, and/or underscores 
- A variable name must start with a letter or an underscore
- A variable name should not be a reserved word

"Reserved words" are:

<div class="verbatim"><pre>
and       del       from      not       while    
as        elif      global    or        with     
assert    else      if        pass      yield    
break     except    import    print              
class     exec      in        raise              
continue  finally   is        return             
def       for       lambda    try</pre></div>

Variables are assigned values with the equal sign (=). Once a variable is created python will store this in memory to be called whenever you like.
"""

x = 3.14159265
y = 7.5
z = x * y * y
print( z )

pi = 3.14159265
radius = 7.5
area_of_circle = pi * radius * radius
print( area_of_circle )

"""As you can see python does not care what name you give to your variables. We recommend you use clear and precise language to describe your variables. Later when you will be working with more complex algorithms or together with other people this will benefit you greatly. """

a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )
print( a * c )

"""It is important to check that you are using the right types of data when creating variables. 

For example, look at the `a * c`statement above it does print the correct results but what is it's type?
"""

type( a * c )

"""Although the result is correct the manner in which it is calculated might not be right. See what happens when you try to use it for further calculations. """

print((a * c) * 3)

"""## 3. Operators

As you can see from the result above, multiplying the result from `a*c` multiplied 1 as a string, as we checked in the cell above that the result from `a*c` was a string. Hence, it is important to keep track of the types of your variables and data to ensure that you will get the result you expect.

In order to perform operations on variables and values, we need some operators as in mathematics. Python has 7 groups of operators and we will go over 6 of them in this notebook. Some of these operators will make more sense as you progress through this notebook with examples of these operators shown inside the example codes.


1. Arithmetic Operators
    * Addition	`x + y	`
    * Subtraction	`x - y	`
    * Multiplication	`x * y	`
    * Division	`x / y	`
    * Modulus	`x % y	`
    * Exponentiation	`x ** y	`

2. Assignment Operators
    * Asign	`x = 5	`
    * Sum with itself and assign	`x += 3` (x  = x + 3)	
    * Subtract from itself and assign	`x -= 3` (x  = x - 3)	
    * Multiply and assign	`x *= 3` (x  = x * 3)	
    * Divide and assign	`x /= 3` (x  = x / 3)	
    * Take the modulus and assign	`x %= 3`	(x = x % 3)	
    * Take the exponential and assign `x **= 3`	(x = x ** 3)

3. Comparison Operators
    * Equal	`x == y`	
    * Not equal	`x != y`	
    * Greater than	`x > y	`
    * Less than	`x < y	`
    * Greater than or equal to `	x >= y`	
    * Less than or equal to `	x <= y`

4. Logical Operators 
    * `and` True if both statements are true	`x < 5 and  x < 10	`
    * `or` True if one of the statements is true `	x < 5 or x < 4`	
    * `not`	Reverse the result, returns False if the result is true	`not(x < 5 and x < 10)`

5. Identity Operators

    * `is` 	True if both variables are the same object	`x is y`	
    * `is not` True if both variables are not the same object	`x is not y`	

6. Membership operators

    * `in`  True if a sequence with the specified value is present in the object	`x in y	`
    * `not in`  True if a sequence with the specified value is not present in the object	`x not in y`

## 4. Functions

As your programs get longer and more complicated, you'll realize you may need to perform the same non-trivial operation multiple times using different values. For that, programming languages including Python provide *functions*. 

A function is a block of code that can be defined somewhere in the code and used in multiple statements by only referencing its name and only runs when it is called. 

In order to write your own functions, you need to define the name of the function, the input values (its parameters), and the value it outputs (returns). A function is defined as the following in Python:

    def <function_name>( <parameter_list> ):
        <statements>
        <return>

For example if you want to calculate the volume of a cylinder different cylinders, instead of writing the formula explicitly every  time you can define a function as the one given below. As parameters, we pass the values that change according to the features of the cylinder we operate on. The values we pass as parameters are used as the variable values inside the function.
"""

def volume_of_cylinder(pi, radius, height):
    volume = pi * radius**2 * height
    return volume

"""It is important that all statements that belong to the function are indented inside the function. This is because Python is **whitespace sensitive** so indentation defines the code blocks."""

def volume_of_cylinder_false(pi, radius, height):
    volume = pi * radius**2 * height
  return volume

volume_of_cylinder(3.14159265, 3, 15) # pi = 3.14159265, radius = 3, height = 15

"""Once you created a function and variables you can play around with it to make it easier to use. For example, it is easier to store the value of pi into a variable so you won't have to type it out every time. Especially for known constants such as Pi, it is good practice to define the variable all capitalized so the reader knows it's value won't change throughout the code, so it's a *constant*"""

PI = 3.14159265
print("Volume:",volume_of_cylinder(PI, 3, 15))
print("Volume:",volume_of_cylinder(PI, 1, 100))
print("Volume:",volume_of_cylinder(PI, 20, 1))

"""Python also features a lot of built-in functions. You can find them all here: https://docs.python.org/3/library/functions.html 

To give some easy examples:
"""

print(max([.0, 4, 10, 200, 56]))
print(min([.0, 4, 10, 200, 56]))
print(sum([.0, 4, 10, 200, 56]))
print(len([.0, 4, 10, 200, 56]))

"""## 5. Conditions

Now that you know how to make a simple function we can go on to make things a bit more fun. You'll notice that for specific values or conditions you might want to have alternative numbers or operations inside the same program. For example consider you write a program that calculates the weight of a person, then the formula you will use in different planets has to be different because of the different gravitational force values. Conditions and if statements provide this functionality using logical rules. 

With conditions, you can write your functions in such a way that it will only return an output if certain requirements are met. To do this we use comparisons with  logical conditions: 

    <    less than
    <=   less than or equal to
    ==   equal to
    >=   equal to or greater than
    >    greater than
    !=   not equal
"""

EARTH_GRAVITY = 9.8
MOON_GRAVITY = 1.62

def calculate_weight(mass, planet):
    gravity = 0
    if planet == 'Earth':
        gravity = EARTH_GRAVITY
    if planet == 'Moon':
        gravity = MOON_GRAVITY

    return mass * gravity

"""Comparisons are also used to trigger functions."""

def tweet_to_long(tweet):
    if len(tweet) <= 140:
        return tweet
    else:
        return "Tweet is too long"

tweet_to_long("So today I went to the park with my dog. I saw a guy on a BMX, he did some very cool tricks. After the park we went for ice cream, I got vanilla and strawberry.")

tweet_to_long("So today I went to the park with my dog. I saw a guy on a BMX, he did some very cool tricks")

"""Besides comparison signs, there are also operators you can use. This is often useful when working with text data.

- **in**: returns True when the parameter is in text
- **not in**: returns True when the parameter is not in the text
- **and**: returns True when both values are True
- **or**: returns True when one of the values is True
- **not**: reverses a True to a False
"""

def letter_A(text):
    if "a" in text:
        return "Booyah!"
    else:
        return ":("

letter_A("Hello World")

def not_letter_A(text):
    if "a" not in text:
        return "Booyah!"
    else:
        return ":("

not_letter_A("Hello World")

def both_A_and_B(text):
    if "a" in text and "b" in text:
        return "Booyah!"
    else:
        return ":("
    
both_A_and_B("Do you know Ali-B")

"""OOPS! that's weird. Even though the letter a and b are in the text the function still returns a sad face. The reason for this is that python is sensitive to capital letters. So an 'a' is not the same as an 'A'. To fix this we can make use of the **or** function."""

def both_A_and_B(text):
    if "a" or "A" in text and "b" or "B" in text:
        return "Booyah!"
    else:
        return ":("
    
both_A_and_B("Do you know Ali-B")

"""It works! How about this one, do you think it will work?"""

def both_A_and_B(text):
    answer = 'Default'
    if "a" or "A" in text and "b" or "B" in text:
        answer = "Booyah!"
    else:
        a = 1
        answer = ":("
    
    return answer
both_A_and_B("Do you know Ali-B")

"""Notice that the statement `answer = ':('` misses a level of indentation to be inside the block of the if statement. Therefore no matter the condition it will be executed inside the code block of the function. To fix the issue, simply indent the statement by 1 level and align it with `a = 1`

## 6. Loops

Another thing you'll notice you'do quite a lot in programming is repeating the same procedure several times. With loops, you can repeat any task written inside the loop countless times. There are two main types of loops in Python: *while* and *for* loops. They essentially have the same functionality but the ways in which they are written and operate are different.

### While Loops
Starting with *while* loops, they repeate the statements inside them while a given condition is correct. The format of while the statement should be as the following,


```
while <conditions>:
    <statements>
```



It comes in very handy when you for example need to write out the entire lyrics of "around the world" by Daft Punk.
"""

def daft_punk():
    num = 1
    while num <= 72:
        print(num,"- Around the world, around the world")
        num += 1

daft_punk()

"""Very handy but you have to be careful. You want to look out for endless loops. An endless loop has no clear ending point which causes it to keep running until it's killed manually. So it is important that you always specify when the loop is finished.

If by mistake you create an endless loop you will have to kill the kernel. You can do this by clicking on "Kernel" in the left top of your screen and proceed to click on "shut down kernel". Let's try this out:
"""

def endless_loop():
    num = 1
    while num >= 0:
        print(num,"- Around the world, around the world")
        num += 1

endless_loop()

"""The reason this loop is endless is that the threshold (num >= 0) is always true. Since num starts at 1 and increases with every iteration the loop will continue to print infinite output.

To give one last example of how a while loop should be done:
"""

def print_multiples_of_7(x):
    count = 0
    while count < x:
        count += 1
        print( count*7 )
    print( "Done" )

print_multiples_of_7(10)

"""### For loops 
So now you know *while* loops and how they can be used. Next up is the **for** loop. A *for* loop has boundaries with a list in which it loops between which makes it a bit easier to use. 

```
for <variable> in <list>:
    <statements>
```



In order to use a **for** loop it is necessary to know the *range()* function. This function creates a list of values between the indicated values and these values are assigned to the iterating variable of the foor loop respectively according to the list.
"""

for i in range(0,3):
    print(i)

for i in range(3,6):
    print(i)

"""When you pass a third variable to the *range()* function this will be the distance between the values in the list. For example when you pass 3 as the third variable, the values in the list will go 3 by 3."""

for i in range(0,10,3):
    print(i)

"""You can also iterate in reverse when you pass a negative value as the third parameter."""

for i in range(10,0,-2):
    print(i)

"""As you can see the **for** loop iterates over all the values in the list that you give. **For** loops are also very useful when you are dealing with text data. This is the case because strings are defined as letter (character) lists on Python. So when you pass a text to a for loop to iterate over, it goes over each letter of the string. We'll talk more about lists in the next section. """

def count_vowels(text):
    vowels = 0
    for i in text:
        if i == "a":
            vowels += 1
        if i == "e":
            vowels += 1
        if i == "o":
            vowels += 1
        if i == "i":
            vowels += 1
        if i == "u":
            vowels += 1
        else:
            continue
    return vowels

count_vowels("hi everyone")

"""## 7. Lists and Dictionaries

The final concepts we'll learn in this notebook are *lists* and *dictionaries*. Both of these structures are designed to store multiple items in a single variable. Lists and dictionaries are similar to each other they are designed to focus on easing different objectives.

### Lists 

Lists are collections of elements that you can store in a variable. The items in a list are ordered. A list can be created with square brackets ([]).
"""

groceries = ['banana','cereal','soda','cake']
groceries

"""You can get the item in a list by using its index. Note that the indeces in lists start from 0 and end at (# of items -1)"""

print("First element is" , groceries[0])
print("Last element is" , groceries[3]) # number of elements (length of the list) is 4 so last item is at 3

"""The fun thing with lists is that you can use loops to go through them:"""

def find_groceries_with_an_e(grocery_list):
    with_e = list()
    for x in grocery_list:
        if 'e' in x:
            with_e.append(x)
    return with_e

find_groceries_with_an_e(groceries)

"""#### List methods

As mentioned above, lists and dictionaries are designed to ease some objectives and in order to achieve this, they need to have some generic built-in *methods* that provide the most commonly used functions of these structures 

For instance, you probably noticed the **.append()** function that was used in the last block. This function is used to add elements to a list.
"""

print(groceries)
groceries.append("bread")
print(groceries)

"""Some other usefull functions are:
- **.insert()**: Adds an element in the desired location.
- **.remove()**: Removes an element.
- **.pop()**: Also removes an element but by index.
- **.sort()**: sorts the list in alphabetic order, or from low to high.

You can find more methods with explanations here: https://docs.python.org/3/tutorial/datastructures.html

Examples:
"""

groceries.insert(2,"milk")
groceries

groceries.remove("cereal")
groceries

groceries.pop(2)
groceries

groceries.sort()
groceries

"""### Dictionaries

Dictionaries differ from lists in the sense that dictionaries are unordered, and they consist of key and value pairs. Dictionaries can be created using the curly brackets ({}).
"""

inventory = {"nike":35,"puma":23,"adidas":80}
inventory["nike"]

"""Dictionaries are useful because you can store values for different keys. So that, later on, you can easily find the information you need. """

for i in inventory:
    print(i, ":", inventory[i])

"""As you can see you can call back the information that you need by using brackets ([]). Adding information to your dictionary works in a similar way:"""

inventory["asics"] = 45
inventory

"""Now let's say, your shop had a good day and you sold 25 Nikes, 7 Pumas, 21 adidas & 10 Asics:"""

inventory["nike"] -= 25 
inventory["puma"] -= 7 
inventory["adidas"] -= 21 
inventory["asics"] -= 10
inventory

"""You can use dictionaries to clean up lists and make them more readable"""

all_shoes = ["nike Air Force 1","nike Air Max 1","Nike Waffle Racer","Nike Cortez","Nike Air Max 90","Nike Air Mag","Nike Air Yeezy","Air Jordan 3","Nike Blazer","Nike Air Max 97","Nike Flyknit Racer",
             "Nike Dunk SB","Nike Air Foamposite","Nike Zoom Spiridon","Nike Air Stab","Nike Kobe 4","Nike Pegasus","Nike Air Presto","Nike Hyperdunk","Nike Kobe 5","Nike Free 5.0",'Air Jordan 6',
             "Nike Air Safari","Nike Challenge Court","Nike Air Mowabb","Nike Air Flight 89","Nike Air Zoom Generation", "Parley x Adidas Ultraboost 6.0.","Adidas Gazelle","Adidas Samba","Adidas Yeezy Powerphase",
             "Adidas NMD_R1","Adidas Pharrell Hu NMD","Adidas Yeezy Boost 350 V2","adidas Superstar", "Puma Future Rider","Puma RS-X","Puma Suede Classic", "Puma RS-X3","Puma Roma","Puma Pacer Next Cage",
             "Puma Smash v2","Puma Mirage Tech"]

def shoes_in_inventory(all_shoes):
    invent = {'nike':0,'puma':0,"adidas":0}
    for shoe in all_shoes:
        if 'nike' in shoe.lower(): #lower() function transforms all letters in a string into lowercase letters
            invent["nike"] += 1
        if 'adidas' in shoe.lower():
            invent["adidas"] += 1
        if 'puma' in shoe.lower():
            invent["puma"] += 1
    return invent

shoes_in_inventory(all_shoes)

"""# Exercises

### 1. Cash

You are given a large number of cents. Write a function that calculates the amount of cash that you have gained in coins (for this exercise you only have to use Euros, 50 cents, 20 cents, and 1 cent). So for example your input is 1753 cents. Then your output should be 17 euros, 1 fifty cents, 0 twenty cents & 3 cents.
"""

def cash_gain(amount):
    euro = amount // 100
    fifty = (amount - (euro * 100)) // 50
    twenty = (amount - (euro * 100) - (fifty * 50)) // 20
    cents = (amount - (euro * 100) - (fifty * 50) - (twenty * 20)) // 1
    return print(euro, "euros,", fifty, "fifty cents,", twenty, "twenty cents &", cents, "cents")
    
cash_gain(1753)

"""### 2. Vowels

Write a function that takes text as an input and returns the number of unique vowels in that text. So for example "I like python, it is so cool" outputs 3 vowels (y is not considered a vowel here)
"""

import numpy as np

def vowel_counter(text):
    vowels = 0
    if "i" in text.lower():
        vowels += 1
    if "e" in text.lower():
        vowels += 1
    if "a" in text.lower():
        vowels += 1
    if "o" in text.lower():
        vowels += 1
    if "u" in text.lower():
        vowels += 1
    return print(vowels, "vowels")

vowel_counter("I like python, it is so cool")

"""### 3. Fibonacci

Write a function that prints all the numbers in a Fibonacci sequence (if you don't know the Fibonacci sequence you can look it up) until it reaches a maximal point. So for example, your input is 50 then the output should be 1,1,2,3,5,8,13,21,34 

**Hint**: use a loop
"""

def print_fibonacci(maxi):
    num1 = 0
    num2 = 1
    print(1)
    while True:
        num3 = num1 + num2
        if num3 > maxi:
            break
        print(num3)
        num1 = num2
        num2 = num3

print_fibonacci(100)

"""### 4.1 Lists & Dictionaries

Write 3 functions that will find the highest, lowest, and most common value in a list of values. So for example your given the input [3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1] then the output should be highest: 78, lowest: -1, most common: 9
"""

def highest(list_in):
    num = 0
    for i in list_in:
        if i > num:
            num = i
    return num

def lowest(list_in):
    num = 9999
    for i in list_in:
        if i < num:
            num = i
    return num

def common(list_in):
    new_dict = {}
    for i in list_in:
        if str(i) in new_dict:
            new_dict[str(i)] += 1
        else:
            new_dict[str(i)] = 1
    most_common = max(new_dict, key=new_dict.get)
    return most_common

def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

print(highest([3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1]))
print(lowest([3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1]))
print(common([3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1]))
print(most_frequent([3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1]))


# same but easier:
print(max([3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1]))
print(min([3,9,5,7,1,9,2,5,9,6,2,33,5,78,9,4,3,9,-1]))

"""### 4.2 Lists & Dictionaries

Write a function that takes a text, splits it into words, and case-insensitively builds a dictionary that stores for every word how often it occurs in the text. Then print all the words with their quantities in alphabetical order. 

**Hint**: look up the .split() and .strip() functions
"""

# AI generated poem:
text = """and soon I am staring out again 
begin to practise my words, expecting my word 
will come. it will not. the wind is calling. 
my friend is near, I hear his breath. 
his breath is not the air. he touches me again with his hands
and tells me I am growing old, he says, far old. 
we travel across an empty field in my heart. 
there is nothing in the dark, I think, but he. 
I close my eyes and try to remember what I was. 
he says it was an important and interesting day, 
because I put in his hands one night 
the box of light that had been a tree."""

def word_counting(text):
    text_list = text.lower().split()
    new_dict = {}
    new_list = []
    for word in text_list:
        new_list.append(word.strip(" ?.,"))
    for word in new_list:
        if word not in new_dict:
            new_dict[word] = 1
        elif word in new_dict:
            new_dict[word] += 1
    keylist = list( new_dict )
    keylist.sort()
    for key in keylist:
        print( key, ':', new_dict[key] )
    return 
    
word_counting(text)

