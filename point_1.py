def basic_operations(number_1:float, number_2:float, operation:str) -> float:
  # Match case for each operation case (+, - , *, /)
  match operation:
    case "+":
      return number_1 + number_2
    case "-":
      return number_1 - number_2
    case "*":
      return number_1 * number_2
    case "/":
      return number_1 / number_2
    case _: # Default case if no one match
      return "Invalid operation"

if __name__ == "__main__":

  # Saving the data provided by the user
  number_1 = float(input("Enter your first number: ")) 
  number_2 = float(input("Enter your second number: "))
  operation : str = input("Enter your operation (+, -, *, /): ")

  #Calling the function
  operations = basic_operations(number_1, number_2, operation)
  print(operations)

