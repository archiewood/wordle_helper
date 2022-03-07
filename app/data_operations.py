import pandas as pd

def update_possible_words(word_list, guess, result):

    for i in range(len(result)):
        if (result[i] == 'Green'):
            word_list = require_letters_by_position(word_list, guess[i], i % 5)
        if (result[i] == 'Yellow'):
            word_list = require_letter(word_list, guess[i])
            word_list = exclude_letters_by_position(word_list, guess[i], i % 5)
        if (result[i] == 'Grey'):
            # # check for double letters
            # if guess.count(guess[i]) > 1:
            #     word_list = word_list
            #     matches = 0

            #     for j in range(len(guess)):
            #         # find the matching letters in the guess
            #         if guess[j] == guess[i]:
            #             # check if the matching letter is yellow or green
            #             if ((result[j] == 'Green') or result[j] == 'Yellow'):
            #                 matches = matches+1
            #                 exclude_double_letters_by_position(
            #                     word_list, guess, result, i % 5, j)

            #     if matches == 0:
            #         word_list = exclude_letter(word_list, guess[i])

            # # if no doubles, proceed as normal
            # else:
            #     word_list = exclude_letter(word_list, guess[i])
            word_list = exclude_letter(word_list, guess[i])
    return word_list

def exclude_letter(word_list, letter):
  if letter == '*': return word_list
  post_filter = word_list[word_list.Word.str.contains(letter) == False]
  return post_filter

def require_letter(word_list, letter):
  if letter == '*': 
    return word_list
  post_filter = word_list[word_list.Word.str.contains(letter) == True]
  return post_filter

def require_letters_by_position(word_list, letter, position):
  if letter == '*': 
    return word_list
  word_list=word_list[word_list['letter'+str(position)]==letter]
  return word_list

def exclude_letters_by_position(word_list, letter, position):
  if letter == '*': 
    return word_list
  word_list=word_list[word_list['letter'+str(position)]!=letter]
  
  return word_list


# def exclude_double_letters_by_position(word_list, guess, result, unmatching_position, matching_position):
#     for i in range(len(guess)):
#         if i != matching_position:
#             word_list = exclude_letters_by_position(
#                 word_list, guess[unmatching_position], i % 5)

#     return word_list

#   def exclude_multiple_letters(word_list, letters):
#     for letter in letters:
#         word_list = exclude_letter(word_list, letter)

#     return word_list



# def include_and_exclude_multiple_letters(word_list, letters_to_include, letters_to_exclude):
#   for letter in letters_to_include:
#     word_list = require_letter(word_list, letter)

#   for letter in letters_to_exclude:
#     word_list = exclude_letter(word_list, letter)

#   return word_list

def count_most_frequent_letters(word_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        word_list[letter] = word_list.Word.str.contains(letter)

    words_letter_count = pd.melt(word_list, id_vars=['Word', 'Frequency', 'letter0', 'letter1',
                                 'letter2', 'letter3', 'letter4'], var_name='letter', value_name='# words containing')

    letters_pivot = words_letter_count.pivot_table(
        values='# words containing', index='letter', aggfunc='sum').sort_values(by='# words containing', ascending=False)

    letters_pivot = letters_pivot[letters_pivot['# words containing'] != 0]

    return letters_pivot
