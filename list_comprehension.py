# [list comprehension] Given a list of strings, create a new list that contains only the strings with more than 5 characters using list comprehension.

def filter_strings(list_of_strings):
    '''
    inp: list of strings
    out: list with with strings more than 5 characters
    '''

    try:
        return [x for x in list_of_strings if len(x)>5]
    except Exception as e:
        return f"Exception: {e}"
    

assert(filter_strings(["Hi","Hello","Welcome","how are you"])==['Welcome', 'how are you'])


# [list comprehension] Given two lists of integers, 
# create a list that contains the product of each element of the first list with the corresponding element in the second list using list comprehension.

list1 = [1,3,5,7]
list2 = [1,2,3,4]

def multiply(list1,list2):
    return [x*y for x,y in zip(list1,list2)]

assert(multiply(list1,list2)==[1,6,15,28])



# [list comprehension] Given three lists list1, list2, and list3, each containing integers, 
# write a Python program using list comprehension to generate a new list of unique triplets (x, y, z) 
# where x is from list1, y is from list2, and z is from list3, such that x + y + z = 0.

list1 = [1, 2, -2, 3, -1]
list2 = [-1, -3, 2, -3, 1]
list3 = [0, 1, 4, -2, -1]

assert([(x,y,z) for x,y,z in zip(list1,list2,list3) if x+y+z==0]==[(1, -1, 0), (2, -3, 1)])
