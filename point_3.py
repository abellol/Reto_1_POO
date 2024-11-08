def is_prime(number:int)->bool: # Function to verify if a number is prime or not
  prime : bool = True 

  # Searching divisors from 2 to the half of the number
  index : int = (number // 2) + 1 
  for i in range(2, index):
    if number % i == 0: # If a divisor is founded, the number isn't prime
      prime = False 
      break
  return prime

def find_primes(numbers:list)->list: # Function to verify if a list have prime numbers
  prime_list : list = [] # Empty list to save prime numbers founded

  # Accesing for every number in the list
  for number in numbers:
    if number == 1: continue # "1" is a special case, it's discarded

    if is_prime(number) == True: # Calling the function to verify each number in the list
      prime_list.append(number) # The prime ones were saved in the empty list
    else:
      continue
  return prime_list

if __name__ == "__main__":
  test_list = [1, 2, 3, 4, 5, 6, 7, 53, 57, 59, 60, 62] # Example list
  primes = find_primes(test_list) # Calling the function
  print(primes)
  