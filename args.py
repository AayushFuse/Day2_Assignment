# [*args] Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. 
# Test your function with various input cases.

def sum_of_all(*val):
    try:
        return sum(val)
    except Exception as e:
        print("Exception: ",e)

try:
    assert(sum_of_all(3,5,6,8)==22)
    assert(sum_of_all(1,2,3,4,5)==15)
    assert(sum_of_all(3,5)==8)

except AssertionError:
    print("AssertionError")

# [*args] Write a Python function concat_strings that takes any number of strings as arguments and returns a single concatenated string.

def concatenate_strings(*val):
    try:
        return ''.join(val)
    except Exception as e:
        print("Exception: ",e)

assert(concatenate_strings("Hi","Hello","How are you")=="HiHelloHow are you")
assert(concatenate_strings("I","Love","You")=="ILoveYou")

