def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))      # Does not execute because 'except' 
                        # clause does not return to 'try' clause

except ZeroDivisionError:
    print('Error: Invalid argument.')
