#!/usr/bin/env python3
import sys
import re


def main():
    matches = re.findall(r"\d+", sys.argv[0])
    day = matches[0]
    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    # FFFBBBFRRR: row 14, column 7, seat ID 119.
    # BBFFBBFRLL: row 102, column 4, seat ID 820.

    with open(f"{day}.txt", "r") as file:
        lines = [line.rstrip("\n") for line in file]

        seats = []
        for seat in lines:

            row = findi(127, seat[:7].replace("F", "0").replace("B", "1"))
            col = findi(7, seat[-3:].replace("L", "0").replace("R", "1"))
            sid = row * 8 + col
            seats.append((row, col, sid))

        max_sid = max([sid for _, __, sid in seats])

        # print(f"part one: {max_sid}")
        by_row = sorted(seats, key=lambda tup: tup[0])
        seats = sorted(seats, key=lambda tup: tup[2])

        front = by_row[0][0]
        back = by_row[-1][0]

        mb = None

        for i, seat in enumerate(seats):
            r, _, sid = seat
            if r != front and r != back:
                mb = sid
                if seats[i + 1][2] == mb + 2:
                    print(f"part two: {mb + 1}")


def findi(start, cmds):
    rang = list(range(start + 1))

    for cmd in cmds:
        if cmd == "0":
            rang = rang[: len(rang) // 2]
        else:
            rang = rang[len(rang) // 2 :]
    return rang[0]


if __name__ == "__main__":
    main()
    print()
