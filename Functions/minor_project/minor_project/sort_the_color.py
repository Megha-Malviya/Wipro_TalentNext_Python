
# Project: 1
# Write a Python function that accepts a hyphen-separated sequence of colors as input 
# and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
# Constraint: All the colors will be completely in either lower case or upper case.
# Sample input1: green-red-yellow-black-white
# Sample output1: black-green-red-white-yellow
# Sample input2: PINK-BLUE-TAN-PURPLE
# Sample output2: BLUE-PINK-PURPLE-TAN

def sort_colors(colors_text):
    colors_list = colors_text.split('-')
    colors_list.sort()
    return '-'.join(colors_list)

first_input = "green-red-yellow-black-white"
print(sort_colors(first_input))

second_input = "PINK-BLUE-TAN-PURPLE"
print(sort_colors(second_input))
