# CS 1430 - Practice 1: Say It Again
#
# Ask for a whole number, then ask for a phrase, then print the phrase
# that many times. The steps are in README.md.
#
# Write your code below this comment.

#Amount of times to print and phrase to print is input
number = int(input("How many times would you like to print the phrase? "))
phrase = input("Please enter a phrase:")

#prints phrase as many times as specified by user
print(phrase * number)