#[set comprehension] Given a list of numbers, create a set using set comprehension that contains only unique even numbers.
list1 = [4,5,4,5,6,7,8,9,10]
print({x for x in list1 if x%2==0})


# [set comprehension] Given a list of words, write a Python program to create a set using set comprehension that contains all the unique characters present in the words.
words = ["Aayush","Abhishek","Prabesh"]
print({y for x in words for y in x})


# [set comprehension] Given two strings, write a Python program to create a set using set comprehension that contains all the characters that are common in both strings.

str1 = "Aayush"
str2 = "Abhishek"

print({i for i in str1 if i in list(str2)})
