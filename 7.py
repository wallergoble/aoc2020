#!/usr/bin/env python3
import sys
import re


def main():
    matches = re.findall(r"\d+", sys.argv[0])
    day = matches[0]
    print("========================")
    print()
    with open(f"{day}.txt", "r") as file:
        bags = [line.rstrip("\n") for line in file]

        baglimits = {}

        for bag in bags:
            l, r = bag.split(" contain ")

            key = l.rsplit(" ", 1)[0]
            _values = re.findall(r"(\d+)\ (\w+\ \w+)", r)
            values = []
            if len(_values) > 0:
                for v in _values:
                    values.append((int(v[0]), v[1]))
            if key in baglimits.values():
                raise Exception("they repeat")

            baglimits[key] = values

        options = []

        # while len(options) != plen:
        #     plen = len(options)
        #     for k, vals in baglimits.items():
        #         for _, v in vals:
        #             if v in options or v == target:
        #                 if k not in options:
        #                     options.append(k)
        answer = 0

        def dive(_color, _amount, total):
            print("args", _color, _amount, total)
            print()
            if len(baglimits[_color]) == 0:
                return total

            sub = 0
            for amount, color in baglimits[_color]:
                sub += amount + amount * dive(color, amount, total)

            return sub

        answer = dive("shiny gold", 1, 0)
        print("hi")
        # stop = all([len(baglimits[k]) == 0 for k in current])
        # while not stop:
        #     current = []
        #     for k in current:
        #         for n, v in baglimits[k]:
        #             answer += n

    p1 = len(options)
    p2 = answer

    print(f"part 1 {p1}")
    print(f"part 2 {p2}")


if __name__ == "__main__":
    main()
    print()
