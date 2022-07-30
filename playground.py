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
sorted_map = dict(sorted(map.items(), key=lambda e: e[1]))
print(sorted_map)

# 5. enumerate()
words = ["while", "if", "else", "for"]
index = enumerate(words)
print(dict(index))