#!/usr/bin/ python3

"""
    Part One:
    1) Turn file input into a list
    2) Iterate over the list comparing a value to the list item before it
    3) Count the times the following value is bigger than the previous
    4) Print the result

    Part Two:
    1) add a window that sums sequential measurements into reading for comparison
"""

from sys import argv

script, input_file = argv
count, window_count, window = 0, 0, 3


class SubSonar:
    def __init__(self, input_file):
        with open(input_file) as depth_reading:
            self.data = depth_reading.read().split("\n")

    def greater_depth(self, first_reading: str, second_reading: str) -> bool:
        return int(second_reading) > int(first_reading)

    def calc_measurement(self, window_size: int = window, start: int = 0) -> int:
        if start <= len(self.data) - window:
            return sum([int(self.data[x]) for x in range(start, start + window)])
        return 0


s1 = SubSonar(input_file)
for position, depth in enumerate(s1.data):
    if s1.greater_depth(s1.data[position - 1], depth) and position > 0:
        count += 1
    if s1.calc_measurement(start=position) < s1.calc_measurement(
        start=position + 1
    ) and position < len(s1.data):
        window_count += 1

print(f"part one: {count}")  # total of depth increases for each specific reading

print(
    f"part two: {window_count}"
)  # total of increases comparing windows of measurement
