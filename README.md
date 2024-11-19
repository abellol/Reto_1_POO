# Reto 1 POO
 Hola, soy **Alejandro Bello León** y esta es mi solución propuesta para el reto #1 de la clase de Programación Orientada a Objetos:

#### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación.
Para la solución se plantea una función que usa un match case que empareja el operador ingresado por el usuario (+, -, *, /) con la operación que se debe realizar, luego realiza la operación correspondiente tomando como operandos los números ingresados por el usuario.

```python
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
```
Y luego en el main del programa, se pide al usuario que ingrese los dos números a operar y la operación que desea realizar.
```python
if __name__ == "__main__":

  # Saving the data provided by the user
  number_1 = float(input("Enter your first number: ")) 
  number_2 = float(input("Enter your second number: "))
  operation : str = input("Enter your operation (+, -, *, /): ")

  #Calling the function
  operations = basic_operations(number_1, number_2, operation)
  print(operations)
```
#### 2. Realice una función que permita validar si una palabra es un palíndromo. (Sin usar slicing)
Para poder verificar si una palabra es un palindromo sin necesidad de usar slicing, consideré que un patrón de acumulación era una buena alternativa, recorriendo las letras de la palabra original de atrás hacía adelante, guardandolas en una variable que será el reverso de la palabra original.

```python
def palindrome(word:str) -> str:
  reversed : str = "" # Variable to save each letter from the reversed word

  # Reversing the word
  for i in range(-1, -(len(word)+1), -1):  
    reversed += (word[i])

  if word == reversed:
    return(f'"{word}" is a palindrome')
  else:
    return(f'"{word}" isnt a palindrome')
```
En el main del programa únicamente se busca pedir una palabra y hacer el llamado a la respectiva función.

```python
if __name__ == "__main__":
  word : str = input("Enter a word to verify if a word is a palindrome: ") # input from de user
  is_palindrome = palindrome(word) # Calling the function
  print(is_palindrome)
```
#### 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Para el desarrollo de este problema se implementaron dos funciones, una para comprobar que un numero sea o no primo; mediante la criba de eratóstenes. Esta función retorna un valor binario (es o no es) para poder simplificar el proceso cuando es con toda la lista de números.

```python
def is_prime(number:int)->bool: # Function to verify if a number is prime or not
  prime : bool = True 

  # Searching divisors from 2 to the half of the number
  index : int = (number // 2) + 1 
  for i in range(2, index):
    if number % i == 0: # If a divisor is founded, the number isn't prime
      prime = False 
      break
  return prime

```
por otro lado, la función principal solo recorre cada elemento (número) de la lista y lo evalua en la función anterior, permitiendo descartar los que no son primos y así poder construir la nueva lista de los números primos en la lista inicial.

```python
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
```

y por último, el main únicamente llama a la función ``find_primes`` para evaluar todos los elementos de la lista ingresada, en este caso es únicamente un ejemplo.

```python
if __name__ == "__main__":
  test_list = [1, 2, 3, 4, 5, 6, 7, 53, 57, 59, 60, 62] # Example list
  primes = find_primes(test_list) # Calling the function
  print(primes)
```
#### 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
En esta solución planteada busca comparar cada posible suma dentro del arreglo con las condiciones dadas, en este caso es que los dos elementos sean consecutivos, por lo que únicamente toca acceder a ellos teniendo cuidado con la forma en que se hace. 

La función sugerida inicia desde el indice ``0`` hasta el ``n-2``, siendo n el total de elementos en la lista, esto nos permite simplemente tomar el indice que está en el ciclo y el que esta a su derecha, es decir, sumarle 1. Luego realiza la suma de los elementos y compara con la suma anterior, haciendo que cuando la suma tenga el valor mas alto posible, sea inmutable.

```python
def higher(numbers : list)-> int: # Function to identify the higher sum between two consecutive numbers
  high = 0 # Starting value for the sume

  # Accesing to every pair of consecutive elements on the list
  for i in range(len(numbers)-1): # Accesing to the index and the next one to the right
    aux = numbers[i] + numbers[i+1] 
    if aux > high: # If the sum is higher than the last value, it replaces it
      high = aux
  return high

```

En el main únicamente se declara una lista de ejemplo, y se hace el llamado a la función.
```python
if __name__ == "__main__":
  test_list = [2, 24, 17, 6, 7, 43] # Example list
  high_sum = higher(test_list) # Call to the function
  print(high_sum)
```
#### 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.
Para la solución de este problema, se utilizaron los diccionarios; una herramienta que sirve para coleccionar datos de una manera ordenada y clara. Allí se guardan las palabras que contienen las mismas letras, utilizando como clave el orden lexicográfico de si mismas.

```python
def same_letters(list_words: list) -> list:
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
```