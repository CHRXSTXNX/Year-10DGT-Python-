# Codes for indenting and width 
# Author: Christine du Preez
# Date: 17th May 2024
# Version: 1.0

# In a function, when hitting the return statement it shall end, breaking out of the loop
# Gold underlines are pipette errors

def number_check(question):

    error = "Please enter a number that is more n zero/n"
    while True:
        
        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else: 
                print(error)

        except ValueError: 
            print(error)

# Main routine goes here, beneath the functions of code
for item in range(0, 2):
    width = number_check("Width: ")
    print(width)

print()

 for item in range(0, 2):
    height = number_check("Height: ")
    print(height)
