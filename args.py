# [*args] Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. 
# Test your function with various input cases.

def sum_of_all(*val):
    '''
    Val should contains numeric values

    returns: Sum of all items
    '''
    try:
        return sum(val)
    except Exception as e:
        return f"Exception: {e}"

try:
    assert(sum_of_all(3,5,6,8)==22)
    assert(sum_of_all(1,2,3,4,5)==15)
    assert(sum_of_all(3,5)==8)

except AssertionError:
    print("AssertionError")

# [*args] Write a Python function concat_strings that takes any number of strings as arguments and returns a single concatenated string.

def concat_strings(*val):
    try:
        return ''.join(val)
    except Exception as e:
        return f"Exception: {e}"

assert(concat_strings("Hi","Hello","How are you")=="HiHelloHow are you")
assert(concat_strings("I","Love","You")=="ILoveYou")

