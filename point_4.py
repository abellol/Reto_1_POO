def higher(numbers : list)-> int: # Function to identify the higher sum between two consecutive numbers
  high = 0 # Starting value for the sume

  # Accesing to every pair of consecutive elements on the list
  for i in range(len(numbers)-1): # Accesing to the index and the next one to the right
    aux = numbers[i] + numbers[i+1] 
    if aux > high: # If the sum is higher than the last value, it replaces it
      high = aux
  return high

if __name__ == "__main__":
  test_list = [2, 24, 17, 6, 7, 43] # Example list
  high_sum = higher(test_list) # Call to the function
  print(high_sum)
