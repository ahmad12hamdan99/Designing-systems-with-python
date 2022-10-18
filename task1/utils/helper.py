
import re

# helper
def validate_input(input_type, value):
    '''
    valditer function to validate the input
    :param input_type: type of validation
    :param value: the input needed to validate
    :return: valid or not (bool)
    '''

    # validate in case of yes/no input
    if input_type == "decision":
        if value.lower() == "yes" or value.lower() == "no":
            return True
        else:
            print("input should be yes/no")
            return False

    # validate in case of 1 or 2 input
    if input_type == "choice1or2":
        if value.isdigit():
            if int(value) == 1 or int(value) == 2:
                return True
            else:
                print("input should be 1 or 2")
                return False
        else:
            print("input should be 1 or 2")
            return False

    # validate in case of choose between 1 and 5
    if input_type == "digit1to5":
        if value.isdigit():
            if int(value) in range(1, 6):
                return True
            else:
                print("input should be an integer between 1 and 5")
                return False
        else:
            print("input should be an integer between 1 and 5")
            return False

    # validate in case of time input in the form hh:dd
    if input_type=="time":
        regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
        p = re.compile(regex)
        if value == "":
            print("Invalid input, use the following form hh:mm")
            return False
        m = re.search(p, value)
        if m is None:
            print("Invalid input, use the following form hh:mm")
            return False
        else:
            return True
