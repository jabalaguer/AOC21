#!/usr/bin/ python3

"""
    Part One:
    1) Turn file input into a list of binary strings
    2) Iterate over the list to calc the most common binary number (0 or 1) at each placeholder
    3) US the most common number to build the gamma binary and the opposite as epsilon binary
    4) Convert the binary numbers to decimal integers
    5) Print gamma * epsilon which is power consumption

    Part Two:
    1) create a recursive function to reduce binary string list base on matching
    2) Oxygen and C02 are mirror images in terms of pattern
    3) Multiply the decimal results of Oxygen and CO2 recursions
"""

from sys import argv

script, input_file = argv


class SubDiagnostic:
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

    def oxygen_generator(self, place: int = 0, lst: list = []) -> int:
        if len(lst) == 1:
            return int(lst[0], 2)
        else:
            lst.sort()
            half, overHalf = len(lst) // 2 - 1, len(lst) // 2
            halfNum = lst[half][place]
            overHalfNum = lst[overHalf][place]
            if halfNum == overHalfNum:
                newlist = list(filter(lambda i: i[place] == halfNum, lst))
                return self.oxygen_generator(place=place + 1, lst=newlist)
            elif halfNum < overHalfNum and len(lst) % 2 == 0:
                newlist = list(filter(lambda i: i[place] == overHalfNum, lst))
                return self.oxygen_generator(place=place + 1, lst=newlist)
            elif (
                len(lst) % 2 == 1
                and halfNum != overHalfNum
                and overHalfNum == lst[overHalf + 1][place]
            ):
                newlist = list(filter(lambda i: i[place] == overHalfNum, lst))
                return self.oxygen_generator(place=place + 1, lst=newlist)

    def CO2_scrubber(self, place: int = 0, lst: list = []) -> int:
        if len(lst) == 1:
            return int(lst[0], 2)
        else:
            lst.sort()
            half, overHalf = len(lst) // 2 - 1, len(lst) // 2
            halfNum = lst[half][place]
            overHalfNum = lst[overHalf][place]
            if halfNum == overHalfNum:
                if int(halfNum) == 1:
                    opp = "0"
                else:
                    opp = "1"
                newlist = list(filter(lambda i: i[place] == opp, lst))
                return self.CO2_scrubber(place=place + 1, lst=newlist)
            elif halfNum < overHalfNum and len(lst) % 2 == 0:
                newlist = list(filter(lambda i: i[place] == halfNum, lst))
                return self.CO2_scrubber(place=place + 1, lst=newlist)
            elif (
                len(lst) % 2 == 1
                and halfNum != overHalfNum
                and overHalfNum == lst[overHalf + 1][place]
            ):
                newlist = list(filter(lambda i: i[place] == halfNum, lst))
                return self.CO2_scrubber(place=place + 1, lst=newlist)


d1 = SubDiagnostic(input_file)
master_reading = d1.power_readings(d1.build_counts())
power_consumption = master_reading["gamma"] * master_reading["epsilon"]
print(f"power consumption: {power_consumption}")

oxy = d1.oxygen_generator(lst=d1.data)
co2 = d1.CO2_scrubber(lst=d1.data)
print(f"life support rating: {oxy * co2}")
