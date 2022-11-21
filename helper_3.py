#! /usr/bin/env python
"""
This is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. It is
distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the code.  If not, see <http://www.gnu.org/licenses/>.

File name: 	helper_3.py
Created:	June 18th, 2020
Author:	Dr. Robert Lyon 

"""
from week_7.Task_03 import decoder


#  import decoder # Use this if compiling / testing from terminal


def main():
    """
    The entry point for program execution.

    :return: N/A
    """
    print("Helper file for Coursework 1.3 - do not modify me!")
    print("The tests below show the input and expected output.\r\r")

    print("Test 1. Input = \"1\"\tOutput = \"1\" \r")
    result = decoder.decode("1")
    if result != "1":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 2. Input = \"2\"\tOutput = \"2\" \r")
    result = decoder.decode("2")
    if result != "2":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 3. Input = \"3\"\tOutput = \"3\" \r")
    result = decoder.decode("3")
    if result != "3":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 4. Input = \"1\"\tOutput = \"4\" \r")
    result = decoder.decode("4")
    if result != "4":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 5. Input = \"10\"\tOutput = \"8\" \r")
    result = decoder.decode("10")
    if result != "8":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 6. Input = \"16\"\tOutput = \"14\" \r")
    result = decoder.decode("16")
    if result != "14":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 7. Input = \"100\"\tOutput = \"64\" \r")
    result = decoder.decode("100")
    if result != "64":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 8. Input = \"34 56\"\tOutput = \"28 46\" \r")
    result = decoder.decode("34 56")
    if result != "28 46":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test 9. Input = \"120 156 206\"\tOutput = \"80 110 134\" \r")
    result = decoder.decode("120 156 206")
    if result != "80 110 134":
        print("\tFailed!")
    else:
        print("\tPassed!")


if __name__ == "__main__":
    # Executes the main method only if run as a script. Will not
    # execute main() if only parts of this file are imported in
    # to another file.
    main()
