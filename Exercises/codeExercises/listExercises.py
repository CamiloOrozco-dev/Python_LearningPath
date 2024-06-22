# Exercise 1
# Create a function that receives 2 lists of numbers and returns the element-wise sum in another list.

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

def sum_elements(list1, list2):
    list3 = []  # Initialize an empty list to store the result
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])  # Add the sum of corresponding elements
    return list3

result = sum_elements(list1, list2)
print(result)  # Print the resulting list

# Exercise 2
# Display the odd numbers from the previous list and the numbers greater than 10.

result1 = list(filter(lambda x: x % 2 == 1, result))  # Filter odd numbers
print(result1)

result2 = list(filter(lambda y: y > 10, result))  # Filter numbers greater than 10
print(result2)

# Exercise 3
# Create a function that receives a list of words and a letter; it should return words starting with that letter.

words = ["python", "java", "javascript", "csharp", "ruby", "html", "css"]
letter = "j"

def words_starting_with_letter(word_list, letter):
    filtered_words = []
    for word in word_list:
        if word.startswith(letter):  
            filtered_words.append(word)
    return filtered_words

result = words_starting_with_letter(words, letter)
print(result)  

resultado = palabras_con_letra_inicial(palabras, letra)
print(resultado)