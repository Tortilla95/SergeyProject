import names 

numberOfNames  = int(input("how many names do you request?"))
genderOption = input("what gender should the names be (male, female, random)?:")
lastName = input("first name, last name or both? (first/last/both):")

nameOption = ()
if lastName == ('both'):
    nameOption = (names.get_full_name)

if lastName == ('last'):
    nameOption = (names.get_last_name)

if lastName == ('first'):
    nameOption = (names.get_first_name)

namelist = []

for x in range(0,numberOfNames):
    namelist.append(nameOption(gender = genderOption))

for namelist in namelist:
    print (namelist)
