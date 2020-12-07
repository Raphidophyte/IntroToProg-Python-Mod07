# ------------------------------------------------- #
# Title: Assignment07
# Description: Example of error handling and pickling
# ChangeLog: (Who, When, What)
# JHerndon,12.06.2020,Attempted to create script
# ------------------------------------------------- #

# Data -------------------------------------------- #
#strFileName = 'Quotient.txt'
#lstCustomer = []

# Processing -------------------------------------- #
#def save_data_to_file(file_name, list_of_data):
#    file = open(file_name, "rb")
#    pickle.dump(list_of_data, file)
#    file.close()

#def read_data_from_file(file_name):
#    file = open(file_name, "rb")
#    list_of_data = pickle.load(file)
#    file.close()
#    return list_of_data

try:
#    file=open("Quotient.txt", "wb")
    file=open("Quotient.txt", "w")
    print("This program will calculate and save a quotient of your making")
    print("Enter a dividend:")
    x = input() #script pauses and captures input
    print("Enter a divisor:")
    y = input() #script pauses and captures input
    x = float(x)
    y = float(y)
    file.write(input("The quotient of {} and {} is: {}".format(str(x),str(y),str(x/y))))
    pickle.dump(file)
    file.close()
except ZeroDivisionError as e:
    print("Please do no use Zero for the second number!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

#save_data_to_file(strFileName, lstCustomer)

# Presentation ------------------------------------ #

#try:
#   quotient = 5/0
#   f = open('SomeFile.txt', 'r+') # the read plus option gives an error if filed does not exist
#    f.write(quotient) # causes an error if the file does not exist
#except ZeroDivisionError as e:
#    print("Please do no use Zero for the second number!")
#    print("Built-In Python error info: ")
#    print(e, e.__doc__, type(e), sep='\n')
