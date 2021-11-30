#!/usr/bin/env python3

import sys
from PasswordGenerator import PasswordGenerator


def main() -> None:
    try:
        digits_quantity: int = int(sys.argv[1])
    except IndexError:
        digits_quantity: int = 32

    try:
        mode: str = sys.argv[2]
    except IndexError:
        mode: str = 'lLns'

    passwordGenerator: PasswordGenerator = PasswordGenerator(digits_quantity, mode)
    print(passwordGenerator.getPassword())


if __name__ == '__main__':
    main()