import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
is_program_on = True


def make_nato():
    word = input('Enter a word: ')
    nato_word = [nato_dict[letter.upper()] for letter in word]
    print(nato_word)


while is_program_on:
    make_nato()
    another_word = input('Do you have another word? (y/n): ')
    if another_word == 'n':
        is_program_on = False
