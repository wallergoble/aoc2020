#!/usr/bin/env python3

import os


def part_one():
    with open("1.txt", "r") as file:
        xs = [int(line.replace("\n", "")) for line in file.readlines()]

        answers = []

        for x in xs:
            for i in range(len(xs)):
                summed = x + xs[i]

                if summed == 2020:
                    answers.append(x)
                    answers.append(xs[i])

        return answers[0] * answers[1]


def part_two():
    with open("1.txt", "r") as file:
        xs = [int(line.replace("\n", "")) for line in file.readlines()]

        answers = []

        for x in xs:
            for i in range(len(xs)):
                for j in range(len(xs)):
                    summed = x + xs[i] + xs[j]

                    if summed == 2020:
                        answers.append(x)
                        answers.append(xs[i])
                        answers.append(xs[j])

        return answers[0] * answers[1] * answers[2]


if __name__ == "__main__":
    res = part_one()
    print(f"answer to part one is {res}")

    res = part_two()
    print(f"answer to part two is {res}")
    print()
