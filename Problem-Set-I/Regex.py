import re

# Input JSON text
text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

# Regex to extract all numbers associated with "id"
regex = r'"id":(\d+)'

# Find all matches
matches = re.findall(regex, text)

# Convert matches to integers
numbers = [int(match) for match in matches]

# Output the list of numbers
print("Numbers with Orange Color Background:")
for number in numbers:
    print(f"\033[48;2;255;165;0m {number} \033[0m")  # Orange background in terminal
