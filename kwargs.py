# [**kwargs] Write a Python function calculate_total_cost that calculates the total cost of items purchased from a store. 
# The function should accept multiple keyword arguments, where the key is the item name, and the value is the item's price. 
# The function should return the total cost of all items.

def calculate_total_cost(**kwargs):
    '''
    Key should contain item name (int,float)
    value should contain the item price (int,float)

    returns: Sum of price of all items
    '''
    try:
        return sum(kwargs.values())
    except Exception as e:
        return("Exception: ",e)


assert(calculate_total_cost(milk = 200,curd=300,paneer=900)==1400)
assert(calculate_total_cost(water = 200,tomatoes=300,rice=100)==600)

# [**kwargs] Create a function create_student_report that takes the student's name as the first argument, 
# the student's age as the second argument, and an arbitrary number of keyword arguments for the subjects and their respective scores. 
# The function should return a dictionary with the student's information and a list of subjects along with their scores.


def create_student_report(name,age,**subjects):
    try:
        return{
            "Name":name,
            "Age":age,
            "Subjects":{sub:score for sub,score in subjects.items()}
            
        }
    except Exception as e:
        return f"Exception: {e}"
    
print(create_student_report("Aayush",22,math=90,science=100,physics=80))

'''
Output
{
    'Name': 'Aayush',
    'Age': 22,
    'Subjects':
    {
        'math': 90,
        'science': 100,
        'physics': 80
    }
}
'''