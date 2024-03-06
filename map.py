# [map] Write a Python function square_numbers that takes a list of integers as input and uses the 
# map function to return a new list containing the square of each element.

def square_numbers(list_of_integers):
    '''
    inp: list_of_integers: list(integer numbers)
    returns: sum of each numbers
    '''
    try:
        return list(map(lambda x:x*x,list_of_integers))
    except Exception as e:
        return f"Exception: {e}"
    


assert(square_numbers([3,4,5,7])==[9,16,25,49])


# [map] Create a function convert_to_uppercase that takes a list of strings as input 
# and uses the map function to return a new list with all the strings converted to uppercase.
def convert_to_uppercase(list_of_strings):
    '''
    inp: list_of_strings: list(strings)
    returns: Uppercase letters of the strings
    '''
    try:
        return list(map(lambda x:x.upper(),list_of_strings))
    except Exception as e:
        return f"Exception: {e}"

assert(convert_to_uppercase(["Hi","hello","how are you"])==['HI', 'HELLO', 'HOW ARE YOU'])