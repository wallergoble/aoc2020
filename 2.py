#!/usr/bin/env python3

import os


def main():
    with open("2.txt", "r") as file:
        passes_and_rules = []
        for line in file.readlines():
            strrange, charwithcolon, password = line.split()
            pmin, pmax = strrange.split("-")
            pchar = charwithcolon.replace(":", "")
            passes_and_rules.append((password, pchar, int(pmin), int(pmax)))

        valid_passwords = []

        for password, char, pmin, pmax in passes_and_rules:
            count = password.count(char)
            if count <= pmax and count >= pmin:
                valid_passwords.append(password)

        print(f"answer to part one is {len(valid_passwords)}")

        valid_passwords_by_position = []
        for password, char, oldmin, oldmax in passes_and_rules:
            pospos = oldmin - 1
            negpos = oldmax - 1

            good_char = password[pospos]
            bad_char = password[negpos]

            count = 0
            if good_char == char:
                count += 1
            if bad_char == char:
                count += 1
            if count == 1:
                valid_passwords_by_position.append(password)

        print(f"answer to part two is {len(valid_passwords_by_position)}")


if __name__ == "__main__":
    main()
    print()
