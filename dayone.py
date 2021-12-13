#!/usr/bin/ python3

"""
    1) Turn file input into a list
    2) Iterate over the list comparing the integer to the list item before it
    3) Count the times the following value is bigger than the previous
    4) Print the result
"""

from sys import argv

script, input_file = argv 
count = 0

class SubSonar:
    def __init__(self, input_file):
        with open(input_file) as depth_reading:
            self.data = depth_reading.read().split("\n")

    def greater_depth(self, first_reading: str, second_reading: str) -> bool:
        return bool(int(second_reading) > int(first_reading))

s1 = SubSonar(input_file)
for position, depth in enumerate(s1.data):
   if s1.greater_depth(s1.data[position-1], depth) and position > 0:
       count += 1

print(f"part one: {count}") # total of depth increases for each specific reading