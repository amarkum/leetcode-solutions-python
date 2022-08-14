# 1. convert list into string
import collections

words = ["l", "e", "e", "t", "c", "o", "d", "e"]
text = "".join(words)
print(text)

# 2. get the last or last n-th element from the list
# expected 2
nums = [2, 3, 5, 6, 7, 8, 2]
print(nums[-1])

# last 3rd element
print(nums[-3])

# 3. Count the element of the list
# time consuming
numbers = [2, 3, 6, 3, 2, 2]
duplicate_count = {number: numbers.count(number) for number in numbers}
print(duplicate_count)

# efficient approach
duplicate_count = collections.defaultdict(int)
for num in numbers:
    duplicate_count[num] = duplicate_count.get(num, 0) + 1
print(dict(duplicate_count))

# 4. Sort dictionary by value
map = {"python": 3, "java": 2, "go": 4}
# key = sort for every x in items(), x[1] > value
sorted_map = dict(sorted(map.items(), key=lambda x: x[1]))
print(sorted_map)

# 5. enumerate()
words = ["while", "if", "else", "for"]
index = enumerate(words)
print(dict(index))

# 6. Find the start index of the substring in the word
str = "leetcode"
start_index = str.find("code")
print(start_index)

# 7. Convert Binary Number to decimal Number
binary = "100"
number = int(binary, 2)
print(number)

# 8. Convert Decimal Number to Binary Number
decimal = 4
binary = bin(decimal)[2:]
print(binary)

# 9. Reverse a string in python
word = "python"
reverse = word[::-1]
print(word, reverse)

# 10. Iterate Python Element in reverse
digits = [1, 2, 3, 4, 5]

# a. classic - step
for i in range(len(digits) - 1, 0, -1):
    print(digits[i])

# b. negate index
for i in range(len(digits)):
    number = digits[-(i + 1)]
    print(number)

# 11. Extract Alpha-numeric characters from String
text = "@$Coding;is$|Fun"
text = "".join([ch for ch in text if ch.isalnum()]).lower()
print(text)

# 12. Methods to perform on the collection
# array
digits = [1, 2, 3, 4, 5]
digits.insert(6, 6)
digits.remove(6)

# set
# seta | setb - union
# seta & setb - intersection
nums = set(digits)
nums.add(7)
nums.discard(7)

# 13. Division Operator
# // - returns to the nearest whole number after division
whole_sum = sum(nums)  # returns the sum of all the numbers
# formula to calculate sum > (n * n+1) // 2

# 14. Count characters in the String
from collections import Counter

counter = Counter(str)
print(counter)
# convert Counter object to Dict
print(dict(counter))
