import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in data.iterrows()}

def translate():
    word = input("Enter Word: ").upper()
    try:
        output = [nato[letter] for letter in word]
        print(output)
    except KeyError:
        print("I said word you dingus. No funny business, just letters.")
        translate()
translate()