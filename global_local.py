def spam():
    global eggs # Takes global scope into local scope
    eggs = 'Hello' # Local variable
    print(eggs)

eggs = 42 # Global variable
spam()
print(eggs)
