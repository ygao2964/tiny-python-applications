import json
from difflib import get_close_matches

data = json.load(open("data.json")) #dict

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: 
        return data[word.upper()]
    elif get_close_matches(word, data.keys()) != []:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exit, pls double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exit, pls double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

