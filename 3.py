#!/usr/bin/env python3

import os


def main():
    with open("3.txt", "r") as file:
        rows = []
        for line in file.read().splitlines():
            repeated_line = line * 100
            rows.append(repeated_line)

        # pointer = 0
        # trees = 0

        # for i, row in enumerate(rows):
        #     if row[pointer] is "#":
        #         trees += 1
        #     pointer += 3

        # result = trees
        # print(f"answer to part one is {result}")

        scenarios = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        ]

        tree_counts = []

        for right, down in scenarios:
            pointer = 0
            trees = 0

            for i, row in enumerate(rows):
                if i % down is 0:
                    if row[pointer] is "#":
                        trees += 1
                    pointer += right
            tree_counts.append(trees)
        print(tree_counts)
        result = mult(*tree_counts)
        print(f"answer to part two is {result}")


def mult(*args):
    p = 1
    for a in args:
        p *= a

    return p


if __name__ == "__main__":
    main()
    print()
