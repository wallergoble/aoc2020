#!/usr/bin/env python3

import re


def main():
    with open("4.txt", "r") as file:
        pps = []
        pp = ""
        for line in file.readlines():
            # print(line)
            if line is not "\n":
                pp += " "
                pp += line.rstrip("\n")

            else:
                pps.append(pp.lstrip())
                pp = ""
        if pp is not "":
            pps.append(pp.lstrip())

        pps = [
            {pair.split(":")[0]: pair.split(":")[1] for pair in pp.split(" ")}
            for pp in pps
        ]

        def hgt(x):
            # hgt (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.

            matches = re.findall(r"\d+|cm|in", x)

            if len(matches) != 2:
                return False

            num, uom = matches
            num = int(num)

            if uom == "cm":
                return between(num, 150, 193)
            if uom == "in":
                return between(num, 59, 76)

            return False

        validations = {
            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            "byr": lambda x: len(x) is 4 and between(int(x), 1920, 2002),
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            "iyr": lambda x: len(x) is 4 and between(int(x), 2010, 2020),
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            "eyr": lambda x: len(x) is 4 and between(int(x), 2020, 2030),
            "hgt": hgt,
            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            "hcl": lambda x: len(re.findall(r"^#[a-z0-9]{6}$", x)) == 1,
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",],
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            "pid": lambda x: len(re.findall(r"^\d{9}$", x)) == 1,
            # cid (Country ID) - ignored, missing or not.
            "cid": lambda _: True,
        }

        count1 = 0
        count2 = 0

        for pp in pps:
            keys = pp.keys()

            if ("cid" not in keys and len(keys) == 7) or len(keys) is 8:
                count1 += 1
                print(pp)
                for k, v in pp.items():
                    # if k == "pid":
                    #     ms = re.findall(r"^\d{9}", v)
                    #     val = len(re.findall(r"^\d{9}$", v)) == 1
                    #     print("this is valid", v, ms, val)
                    valid = validations[k](v)
                    print(k, v, valid)
                print()
                print()
                if all([validations[k](v) for k, v in pp.items()]):
                    count2 += 1

        print(f"the answer to part one is {count1}")
        print(f"the answer to part two is {count2}")

        # Part 2


def between(num, min, max):
    return num >= min and num <= max


if __name__ == "__main__":

    main()
    print()
    print()
    print()
    print()
