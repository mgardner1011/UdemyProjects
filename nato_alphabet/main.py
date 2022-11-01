import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
is_program_on = True


def make_nato():
    word = input('Enter a word: ')
    try:
        nato_word = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print('Input must contain only letters')
        make_nato()
    else:
        print(nato_word)


while is_program_on:
    make_nato()
    another_word = input('Do you have another word? (y/n): ')
    if another_word.lower() == 'n':
        is_program_on = False
