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

def twoRandoms(coll):
    # return a list of 2 random lowerCase letters
    return random.choices(coll, k=2)


# concatenate the returned strings in to one string
temp = twoRandoms(lowerCase) + twoRandoms(upperCase) + twoRandoms(digits) + twoRandoms(syms)
random.shuffle(temp)  # shuffle the final string

# join the random list elements into a string
password = "".join(temp)
print (password)