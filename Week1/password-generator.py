#! /usr/bin/python3
import string, random
# A helper function to split a string
def split(all):
    return [char for char in all]

all_strings = split(string.printable)
# create lists to store each type of string
digits = all_strings[0:10]
lowerCase = all_strings[10:36]
upperCase = all_strings[36:62]
syms = all_strings[62:94]

def lowerLetters(lower):
    # return a list of 2 random lowerCase letters
    return random.choices(lower, k=2)
def upperLetters(upper):
    # return a list of 2 random upperCase letters
    return random.choices(upper, k=2)
def numbers(vals):
    # return a list 2 digits of type string
    return random.choices(vals, k=2)
def symbols(syms):
    # return a list of 2 random symbols 'space' excluded
    return random.choices(syms, k=2)

# concatenate the returned strings in to one string
temp = lowerLetters(lowerCase) + upperLetters(upperCase) + numbers(digits) + symbols(syms)
random.shuffle(temp)  # shuffle the final string

# join the random list elements into a string
password = "".join(temp)
print (password)