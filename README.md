# Python Common Operations README

This README provides a quick reference for frequently used Python operations, such as accessing elements, string manipulations, sorting, searching, and more.

## Table of Contents

1. [Accessing Elements](#accessing-elements)
2. [String Manipulation](#string-manipulation)
3. [Sorting Lists](#sorting-lists)
4. [Searching in Collections](#searching-in-collections)
5. [Mathematical Operations](#mathematical-operations)
6. [Data Structures](#data-structures)
7. [File Handling](#file-handling)
8. [Error Handling](#error-handling)
9. [Miscellaneous](#miscellaneous)

---

## Accessing Elements

### Get the Last Element of a List

```python
my_list = [10, 20, 30, 40, 50]
last_element = my_list[-1]  # Output: 50
```

### Get the First Element of a List

```python
first_element = my_list[0]  # Output: 10
```

### Get a Subset of a List (Slicing)

```python
subset = my_list[1:4]  # Output: [20, 30, 40]
```

---

## String Manipulation

### Reverse a String

```python
my_string = "Python"
reversed_string = my_string[::-1]  # Output: "nohtyP"
```

### Convert to Uppercase

```python
uppercase_string = my_string.upper()  # Output: "PYTHON"
```

### Convert to Lowercase

```python
lowercase_string = my_string.lower()  # Output: "python"
```

### Check if a String Contains a Substring

```python
if "Py" in my_string:
    print("Substring found!")  # Output: "Substring found!"
```

---

## Sorting Lists

### Sort a List in Ascending Order

```python
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Output: [1, 2, 5, 5, 6, 9]
```

### Sort a List in Descending Order

```python
sorted_desc = sorted(numbers, reverse=True)  # Output: [9, 6, 5, 5, 2, 1]
```

### Sort a List In-Place

```python
numbers.sort()  # numbers is now [1, 2, 5, 5, 6, 9]
```

---

## Searching in Collections

### Check If an Element Exists in a List

```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list!")  # Output: "Banana is in the list!"
```

### Find the Index of an Element

```python
index = fruits.index("banana")  # Output: 1
```

---

## Mathematical Operations

### Find the Maximum and Minimum Value

```python
max_value = max(numbers)  # Output: 9
min_value = min(numbers)  # Output: 1
```

### Calculate the Sum of a List

```python
total = sum(numbers)  # Output: 28
```

### Generate a Range of Numbers

```python
num_range = list(range(1, 11))  # Output: [1, 2, 3, ..., 10]
```

---

## Data Structures

### Create a Dictionary

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
```

### Get a Value from a Dictionary

```python
name = person.get("name")  # Output: "Alice"
```

### Remove a Key from a Dictionary

```python
person.pop("age")  # Removes "age" key from dictionary
```

---

## File Handling

### Read a File

```python
with open("example.txt", "r") as file:
    content = file.read()
```

### Write to a File

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
```

### Append to a File

```python
with open("example.txt", "a") as file:
    file.write("
Adding more content.")
```

---

## Error Handling

### Try-Except Block

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catch Multiple Exceptions

```python
try:
    x = int("text")
except (ValueError, TypeError):
    print("Invalid conversion!")
```

---

## Miscellaneous

### Get Unique Elements from a List

```python
unique_numbers = list(set(numbers))  # Output: [1, 2, 5, 6, 9]
```

### Swap Two Variables

```python
a, b = 5, 10
a, b = b, a  # Now a = 10, b = 5
```

### List Comprehensions

```python
squares = [x ** 2 for x in range(1, 6)]  # Output: [1, 4, 9, 16, 25]
```

---

## Conclusion

These are some of the most commonly used Python operations. Whether you're working with lists, strings, dictionaries, or files, these quick references will help you write efficient Python code.

Happy coding!
