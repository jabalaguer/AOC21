#!/usr/bin/ python3

"""
    Part One:
    1) Turn file input into a list of tuples
    2) Iterate over the list using the directions to populate depth and distance (horizon)
    3) Multiply the final depth and horizon
    4) Print the result

    Part Two:
    1) mod the navigate function to use aim and rerun depth * horizon
"""

from sys import argv

script, input_file = argv

class SubPilot:
    def __init__(self, input_file):
        with open(input_file) as depth_reading:
            self.moves = [tuple(x.split(" ")) for x in depth_reading.read().split("\n")]
    
    def navigate(self, depth: int = 0, horizon: int = 0) -> tuple:
        for move in self.moves:
            if move[0] == "up":
                depth -= int(move[1])
            if move[0] == "down":
                depth += int(move[1])
            if move[0] == "forward":
                horizon += int(move[1])
        return (depth, horizon)
    
    def aim_navigate(self, depth: int = 0, horizon: int = 0, aim:int = 0) -> tuple:
        for move in self.moves:
            if move[0] == "up":
                aim -= int(move[1])
                print(aim)
            if move[0] == "down":
                aim += int(move[1])
                print(aim)
            if move[0] == "forward":
                horizon += int(move[1])
                depth += aim * int(move[1])
        return (depth, horizon)   


p1 = SubPilot(input_file)
nav1, nav2 = p1.navigate(), p1.aim_navigate()
print(f"part one: {nav1[0] * nav1[1]}")
print(f"part two: {nav2[0] * nav2[1]}")
