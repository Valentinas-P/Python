import pandas

# TODO 1. Create a dictionary in this format:
alphabetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabetic_dict = {row.letter: row.code for index, row in alphabetic_data.iterrows()}
print(alphabetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type your name: ").strip("").upper()
letters_to_start = list(user_input)

new_list = [alphabetic_dict[letter] for letter in user_input]
print(new_list)
