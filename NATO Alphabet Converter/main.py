import pandas

alphabetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabetic_dict = {row.letter: row.code for index, row in alphabetic_data.iterrows()}

def nato_alphabet():
    try:
        user_input = input("Type your name: ").strip("").upper()
        new_list = [alphabetic_dict[letter] for letter in user_input]
        print(new_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alphabet()


nato_alphabet()
