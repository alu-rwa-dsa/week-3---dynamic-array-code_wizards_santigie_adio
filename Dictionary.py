Dictionary={"Name":"Adedehi","Class":"1","Course":"Computer science"}
def add(keys,Values):
    Dictionary[keys]=Values
    print(Dictionary)

def remove(keys):
    Dictionary.pop(keys)
    print(Dictionary)


def modify(keys,newvalues):
    Dictionary[keys]=newvalues
    print(Dictionary)


def lookup(Keys):
    Keys=Dictionary.keys()
    print(Keys)


lookup("Name")

modify("Name","Aderinsola")
add("Nationality","Nigerian")

remove("Course")