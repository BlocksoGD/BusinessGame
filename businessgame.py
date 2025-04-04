import random

def setName():
    while True: 
        name = input("Enter your chartacter's first name: ").lower().strip()
        if name.isalpha() == False:
            print(f"Please enter your name, and only in alphabets. Y1our response '{name}' contains invalid characters.")
        else:
            name = name.capitalize()
            print(f"You chose the name: {name}.")
            return name
        
def setCommodity(size):
    while True:
        pass

def setBusinessSize():
    print("""
--------------------------------------------------------------------------------------------
 - Please enter a size for your business, numbers from 1 to 4. 
                     
 - 1. Small scale business: Singular shop, little to no reach to broader markets. [Hard]
                     
 - 2. Medium size: Single, larger shop, with good reputation in the city, and good reach
                        in local markets. [Medium]
                     
 - 3. Nation-wide: Multiple shops accross the nation, big name and good reputation. [Easy]
                     
 - 4. MNC: Multi-National company. A big, reputed company in the world. [Easiest]
--------------------------------------------------------------------------------------------
""")
    while True:
        size = input("Please enter a number from 1 to 4. ")
        if size.isdigit():
            if size == "1":
                size = "Small-scale business"
                break
            elif size == "2":
                size = "Medium-size business"
                break
            elif size == "3":
                size = "Nation-wide business"
                break
            elif size == "4":
                size = "MNC"
                break          
            else:
                print(f"The number must be between 1 and 4.")

        else:
            print(f"Invalid response, '{size}', please enter a number from 1 to 4.")
    print(f"Your company size is: {size}.")
    return size

playerName = setName()

print(f"""
--------------------------------------------------------------------------------------------
-Welcome to the business game, {playerName}! Your dad has just retired from his [commodity]
 business. Now, it is your duty to grow it, currently it is a [size?] 
--------------------------------------------------------------------------------------------""")

size = setBusinessSize()
commodity = setCommodity(size)