# [reduce] Write a Python function calculate_factorial that takes an integer as input 
# and uses the reduce function to return the factorial of that number.

from functools import reduce

def calculate_factorial(number):
    '''
    inp: integer
    output: factorial of a number
    '''

    try:
        return reduce((lambda x,y:x*y),range(1,number+1))
    except Exception as e:
        return f"Exception: {e}"
    


assert(calculate_factorial(6)==720)
assert(calculate_factorial(5)==120)


# [reduce] Implement a function called concatenate_strings that takes a list of strings as input and
# uses the reduce function to return a single string containing the concatenation of all the elements.

def concatenate_strings(list_strings):
    '''
    inp: List of strings
    output concatenated string
    '''

    try:
        return reduce((lambda x,y:x+y),list_strings)
    except Exception as e:
        return f"Exception: {e}"
    

assert(concatenate_strings(["I","love","you"])=="Iloveyou")
assert(concatenate_strings(["my","name","is","aayush"])=="mynameisaayush")