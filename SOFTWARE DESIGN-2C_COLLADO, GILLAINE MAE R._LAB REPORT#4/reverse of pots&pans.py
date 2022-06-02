def reverseRecursion(given_string):
    stringLen = len(given_string)

    if stringLen == 1:
        return given_string
    else:

        return reverseRecursion(given_string[1:]) + given_string[0]


givenstring = 'Gillaine Mae'

print('The original given string =', givenstring)

print('Reverse word {after reversing} = ',
      reverseRecursion(givenstring))

