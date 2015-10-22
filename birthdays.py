# Birthday database
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# Prompts for name. Program terminates when blank.
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

# Prints birthday of user input found in dictionary. If not found, prompts for new birthday
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
