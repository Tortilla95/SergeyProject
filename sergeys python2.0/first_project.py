first_name = input('enter your first name:')
last_name = input('enter your last name:')

first_name = first_name.title()
last_name = last_name.title()

print (first_name, last_name)
name = input('is this right? (Y/N)')

if name == 'Y':
    print ("Your name is:",first_name, last_name)
 