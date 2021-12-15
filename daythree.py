#!/usr/bin/ python3

"""
    Part One:
    1) Turn file input into a list of binary strings
    2) Iterate over the list to calc the most common binary number (0 or 1) at each placeholder
    3) US the most common number to build the gamma binary and the opposite as epsilon binary
    4) Convert the binary numbers to decimal integers
    5) Print gamma * epsilon which is power consumption

    Part Two:
    1) add a window that sums sequential measurements into reading for comparison
"""

from sys import argv

script, input_file = argv


class PowerDiagnostic:
    def __init__(self, input_file):
        with open(input_file) as depth_reading:
            self.data = depth_reading.read().split("\n")

        # Build a dict of tuples to hold counts based on binary length
        self.bin_tally = dict(
            zip([x for x in range(len(self.data[0]))], [[0, 0]] * len(self.data[0]))
        )

    def build_counts(self) -> dict:
        for line in self.data:
            for place, num in enumerate(line):
                if int(num) == 1:
                    self.bin_tally[place] = [
                        self.bin_tally[place][0],
                        self.bin_tally[place][1] + 1,
                    ]
                if int(num) == 0:
                    self.bin_tally[place] = [
                        self.bin_tally[place][0] + 1,
                        self.bin_tally[place][1],
                    ]
        return self.bin_tally

    def power_readings(self, counts: dict) -> dict:
        readings = dict(zip(["gamma", "epsilon"], [""] * 2))
        for x in counts:
            if counts[x][0] > counts[x][1]:
                readings["gamma"] += "0"
                readings["epsilon"] += "1"
            if counts[x][1] > counts[x][0]:
                readings["gamma"] += "1"
                readings["epsilon"] += "0"
        readings["gamma"], readings["epsilon"] = int(readings["gamma"], 2), int(
            readings["epsilon"], 2
        )
        return readings


d1 = PowerDiagnostic(input_file)
master_reading = d1.power_readings(d1.build_counts())
power_consumption = master_reading["gamma"] * master_reading["epsilon"]
print(f"part one: {power_consumption}")
