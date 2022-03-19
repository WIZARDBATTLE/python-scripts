import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter Word: ").upper()
output = [nato[letter] for letter in word]

print(output)