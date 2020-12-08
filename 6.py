#!/usr/bin/env python3
import sys
import re


def main():
    matches = re.findall(r"\d+", sys.argv[0])
    day = matches[0]

    with open(f"{day}.txt", "r") as file:
        lines = [line.rstrip("\n") for line in file]

    groups = []
    group = []

    for line in lines:
        if line != "":
            group.append(line)
        else:
            groups.append(group)
            group = []

    groups.append(group)

    p1 = 0
    p2 = 0

    for group in groups:
        p1 += len(set("".join(group)))
        print(group)
        sets = [set(person) for person in group]
        print(sets)
        us = set.intersection(*sets)
        print(len(us), us)
        print()
        p2 += len(us)

    print(f"part 1 {p1}")
    print(f"part 2 {p2}")


if __name__ == "__main__":
    main()
    print()
