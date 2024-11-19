def same_letters(list_words: list) -> list:
  """
  Function to find the words with the same letters in a list.

  Args:
    list_words: A list with words (list)

  Returns:
    The function returns a list with the words that have the same letters.
  """
  words = {} # empty dictionary to save the words with the same lexicographic order
  result = [] # empty list to save the words with the same letters

  for word in list_words:
    valor = "".join(sorted(word)) # Ordering the word by lexicographic order and using it as key, and saving the original word
    if valor in words.keys():
      words[valor] += [word]
    else:
      words[valor] = [word]
  
  for value in words.values(): # if the key (the lexicographic order of a word) has two or more words, they have the same letters
    if len(value) >= 2:
      result += value

  return result 

if __name__ == "__main__":
  test_list : list = ["roma", "amor", "perro", "ropa", "pora", "mora", "juan", "porre"]
  print(same_letters(test_list))
