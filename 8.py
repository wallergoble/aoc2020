#!/usr/bin/env python3
import sys
import re
from copy import deepcopy


def main():
    print("========================")
    print()
    # p1 = acc
    p2 = None
    day = re.findall(r"\d+", sys.argv[0])[0]

    ls = []
    with open(f"{day}.txt", "r") as file:
        matches = [
            re.fullmatch(r"(.+?) (\+|\-)(\d+)", line.rstrip("\n")).groups()
            for line in file
            if line.strip() != ""
        ]
        for match in matches:
            ls.append([match[0], match[1], int(match[2])])

    def tryy(lines):
        visited = {}
        pointer = 0
        acc = 0
        terminated_peacefully = False
        while True:
            if pointer >= len(lines):
                terminated_peacefully = True
                break

            act, op, num = lines[pointer]

            count = visited.get(pointer) or 0
            visited[pointer] = count + 1

            if visited[pointer] == 2:
                break

            if act == "nop":
                pointer += 1

            if act == "jmp":
                if num == 0:
                    break
                pointer = math(op, pointer, num)
                if pointer < 0:
                    raise Exception("uh oh")

            if act == "acc":
                acc = math(op, acc, num)
                pointer += 1

        return terminated_peacefully, acc

    for i, l in enumerate(ls):
        action = l[0]

        if action == "jmp" or action == "nop":
            mutated_lines = deepcopy(ls)
            mutated_lines[i][0] = "jmp" if action == "nop" else "nop"
            good, acc = tryy(mutated_lines)

            if good is True:
                p2 = acc
                break

    # p1 = acc

    # print(f"part 1 {p1}")
    print(f"part 2 {p2}")


def math(str_op, n1, n2):
    # Polish notation, baby
    if str_op == "+":
        return n1 + n2
    else:
        return n1 - n2


if __name__ == "__main__":
    main()
    print()
