# 1. convert list into string
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
numbers = [2, 3, 6, 3, 2, 2]
duplicate_count = {number: numbers.count(number) for number in numbers}
print(duplicate_count)

# 4. Sort dictionary by value
map = {"python": 3, "java": 2, "go": 4}
sorted_map = dict(sorted(map.items(), key=lambda e: e[1]))
print(sorted_map)