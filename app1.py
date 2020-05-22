# Import json library to store the list of word
# Import get_close_matches to calculate the ratio
import json
from difflib import get_close_matches

# Open .json file and save it in a variable "data"
data = json.load(open("data.json"))


def eng_word(word):
    word = word.lower()  # convert any entered word into lower case to find it easily.
    if word in data:
        return data[word]
    elif word.title() in data:  # if the word is capitalized return it with the capital
        return data[word.title()]
    elif word.upper() in data:  # in case that the word is in uppercase
        return data[word.upper()]
# Calculate the ratio to get the closer similarity word to search
    elif len(get_close_matches(word, data.keys())) > 0:
        # Ask user about his choice in give him hint.
        yn = input("Did you mean %s instead? Enter Y if yes, or N if No: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]  # return the hint in case tha he/she accepts the clue.
        elif yn == "N":
            return "Sorry, this word doesn't exist. Please double check it"
        else:
            return "We don't understand your entry."
    else:
        return "Sorry, this word doesn't exist. Please double check it."


word = input("Enter an English word: ")
# Condition test in case that a word has several meanings.
output = eng_word(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



