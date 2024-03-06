# [dictionary comprehension] Given two lists
# one containing keys and another containing values, create a dictionary using dictionary comprehension.

key = ["fruits","vegetable","sports","singer"]
values = ["apple","carrot","football","Nabin K Bhattarai"]

print({key:values for key,values in zip(key,values)})

''' Output {'fruits': 'apple', 'vegetable': 'carrot', 'sports': 'football', 'singer': 'Nabin K Bhattarai'} '''



# [dictionary comprehension] Given a dictionary with students' names as keys and their respective scores as values,
# create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.
students = {"Aayush":90,"Ozil":80,"Saka":79,"Rice":99}
print({name:score for name,score in students.items() if score>80})
'''Output {'Aayush': 90, 'Rice': 99}'''

# [dictionary comprehension] Create a dictionary using dictionary comprehension to represent the ASCII values of lowercase alphabets
# (a-z) where the keys are the alphabets, and the values are their corresponding ASCII values.

import string

print({x:ord(x) for x in string.ascii_lowercase})

