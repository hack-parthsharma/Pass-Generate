#!/usr/bin/python3
# Lesser General Public License (LGPL) v3.0 .
# The project has been developed by Saman Ebrahimnezhad .
# Created at Iran (IR) .
# Python 3 .

import sys
import random
import string

class PassGenerate:

    def __init__(self):

        # figlet used for ASCII

        icon = open('/etc/PassGenerate/icon.txt', 'r')

        icon_contents = icon.read()

        print(icon_contents)

        icon.close()

        size = 0

        if len(sys.argv) < 2:
            sizeInput = input("Enter the size of password: ")
            size = int(sizeInput)
        else:
            size = sys.argv[1]

        print(self.generate(size))

    def generate(self, size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))

def main():
    app = PassGenerate()

if __name__ == '__main__':
    main()
