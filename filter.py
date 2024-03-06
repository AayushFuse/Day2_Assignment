# [filter] Implement a function called filter_prime_numbers that takes a list of integers as input 
# and uses the filter function to return a new list containing only the prime numbers.

def is_prime(num):
    '''
    for checking a prime
    inp: integer
    output: True if prime else False
    '''
    if num in [0,1]:
         return False
    for i in range(num):
         if i==0 or i==1:
              continue
         else:
              if num % i == 0:
                   return False
    return True

def filter_prime_numbers(numbers):
   try:
        return list(filter(is_prime,numbers)) 
   except Exception as e: 
        return f"Exception: {e}"



assert(filter_prime_numbers([1,2,3,4,89])==[2, 3, 89])


# [filter] Write a Python function filter_long_strings that takes a list of strings as input
# and uses the filter function to return a new list containing strings with more than 5 characters.

def filter_long_strings(list_of_strings):
     '''
     inp: list of strings
     returns: strings with more than 5 characters
     '''
     try:
        return list(filter(lambda x:len(x)>5,list_of_strings))
     except Exception as e: 
        return f"Exception: {e}"


assert(filter_long_strings(["hi","Helloooo","Aayush","Hello"])==['Helloooo', 'Aayush'])