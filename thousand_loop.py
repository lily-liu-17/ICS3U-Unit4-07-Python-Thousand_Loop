#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program will print 1000-2000

import constants1


def main():
    # this program will 1000-2000
    output = " "

    # process & output
    for counter in range(1000, constants1.END + 1):
        if counter % 5 == 0:
            output = str(counter)
        else:
            output += " " + str(counter)

        if counter % 5 == 4 or counter == constants1.END:
            print(output)

    print("\nDone.")


if __name__ == "__main__":
    main()
