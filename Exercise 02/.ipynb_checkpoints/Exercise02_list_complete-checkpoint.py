# ## Exercise
# Let's practice some list comprehension. These tasks were taken from [here](https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a) (go and give him a star ;)).

# +
# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# -

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
uppercased_fruits= [fruit.upper() for fruit in fruits];print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits=[capital[0].upper()+capital[1:] for capital in fruits]; print (capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_more_than_two_vowels=[vowels for vowels in fruits if sum (1 for letter in vowels if letter in "aeiou")>2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']


fruits_with_only_two_vowels=[vowels for vowels in fruits if sum (1 for letter in vowels if letter in "aeiou") ==2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters


fruit_with_more_than_5_characters=[letter for letter in fruits if sum (1 for cha in letter) >5]
print(fruit_with_more_than_5_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters


fruit_with_exactly_5_characters=[letter for letter in fruits if sum (1 for cha in letter) ==5]
print(fruit_with_exactly_5_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters


fruit_with_less_than_5_characters=[letter for letter in fruits if sum (1 for cha in letter) <5]
print(fruit_with_less_than_5_characters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
number_of_characters_in_each_fruit=[len(number) for number in fruits]
print(number_of_characters_in_each_fruit)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_letter_a=[letter for letter in fruits if 'a' in letter] 
print(fruits_with_letter_a)

# +
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
# -

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
even_numbers=[letter for letter in fruits if sum (1 for cha in letter) % 2 ==0]
print(even_numbers)

numebers=[1,2,3,4,5,6,7, 9,10]
even_numbers=[letter for letter in numebers if letter % 2 ==0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers


numebers=[1,2,3,4,5,6,7, 9,10,11]
odd_numbers=[letter for letter in numebers if letter % 2 !=0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers


numebers=[1,2,3,4,-5,6,7, 9,-10,11]
positive_numbers=[letter for letter in numebers if letter>0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers


numebers=[1,2,3,4,-5,6,7, 9,-10,11]
negative_numbers=[letter for letter in numebers if letter<0]
print(negative_numbers)

# # When to use list comprehension and when to use for loops?

import this


