def divide(a,b):
    """ this method is meant to be called making a deliberate error, caught in a try block """
    try:
        return a / b
    except:
        print('Divide by zero error caught')


print(divide(1,0))
