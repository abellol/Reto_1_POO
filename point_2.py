def palindrome(word:str) -> str:
  reversed : str = "" # Variable to save each letter from the reversed word

  # Reversing the word
  for i in range(-1, -(len(word)+1), -1):  
    reversed += (word[i])

  if word == reversed:
    return(f'"{word}" is a palindrome')
  else:
    return(f'"{word}" isnt a palindrome')
  
if __name__ == "__main__":
  word : str = input("Enter a word to verify if a word is a palindrome: ") # input from de user
  is_palindrome = palindrome(word) # Calling the function
  print(is_palindrome)
  
  
