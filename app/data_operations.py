import logging


def update_possible_words(word_list, guess, result):

    for i in range(len(result)):
        if (result[i] == 'Green'):
            word_list = require_letters_by_position(word_list, guess[i], i)
        if (result[i] == 'Yellow'):
            word_list = require_letter(word_list, guess[i])
            word_list = exclude_letters_by_position(word_list, guess[i], i)
        if (result[i] == 'Grey'):
            word_list = exclude_letter(word_list, guess[i])
    return word_list


def exclude_letter(word_list, letter):
    if letter == '*': return word_list
    post_filter = word_list[word_list.Word.str.contains(letter) == False]
    return post_filter


def exclude_multiple_letters(word_list, letters):
    for letter in letters:
        word_list = exclude_letter(word_list, letter)

    return word_list


def require_letter(word_list, letter):
  if letter == '*': 
    return word_list
  post_filter = word_list[word_list.Word.str.contains(letter) == True]
  return post_filter


def include_and_exclude_multiple_letters(word_list, letters_to_include, letters_to_exclude):
  for letter in letters_to_include:
    word_list = require_letter(word_list, letter)
  
  for letter in letters_to_exclude:
    word_list = exclude_letter(word_list, letter)
  
  return word_list

def require_letters_by_position(word_list, letter, position):

  if letter == '*': return word_list
  word_list=word_list[word_list['letter'+str(position)]==letter]
  
  return word_list

def exclude_letters_by_position(word_list, letter, position):
  if letter == '*': 
    return word_list
  word_list=word_list[word_list['letter'+str(position)]!=letter]
  
  return word_list