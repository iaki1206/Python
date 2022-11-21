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

File name: 	helper_2.py
Created:	June 18th, 2020
Author:	Dr. Robert Lyon



"""
from week_6.Task_02 import control
#  import control # Use this if compiling / testing from terminal


def main():
    """
    The entry point for program execution.

    :return: N/A
    """
    print("Helper file for Coursework 1.2 - do not modify me!")
    print("The tests below show the input and expected output.\r\r")

    # Some variables which help during testing
    t = 0.1  # the collision threshold in metres.
    gt_ct = t + 0.01  # greater than collision threshold.
    et_ct = t  # equal to collision threshold.
    lt_ct = t - 0.01  # less than collision threshold.

    print("Test Scenario 1.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"S\" \r")
    result = control.choose_action(lt_ct, gt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "S":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 2.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"W\" \r")
    result = control.choose_action(gt_ct, lt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "W":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 3.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"N\" \r")
    result = control.choose_action(gt_ct, gt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "N":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 4.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"E\" \r")
    result = control.choose_action(gt_ct, gt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "E":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 5.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"SW\" \r")
    result = control.choose_action(lt_ct, lt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "SW":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 6.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"E or W\" \r")
    result = control.choose_action(lt_ct, gt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "E or W":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 7.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"SE\" \r")
    result = control.choose_action(lt_ct, gt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "SE":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 8.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"NW\" \r")
    result = control.choose_action(gt_ct, lt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "NW":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 9.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"N or S\" \r")
    result = control.choose_action(gt_ct, lt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "N or S":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 10.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"NE\" \r")
    result = control.choose_action(gt_ct, gt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "NE":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 11.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"S\" \r")
    result = control.choose_action(lt_ct, lt_ct, gt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "S":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 12.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"W\" \r")
    result = control.choose_action(lt_ct, lt_ct, lt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "W":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 13.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"E\" \r")
    result = control.choose_action(lt_ct, gt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "E":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 14.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"N\" \r")
    result = control.choose_action(gt_ct, lt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "N":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 15.")
    print("\tSensor 1 Input = " + str(gt_ct))
    print("\tSensor 2 Input = " + str(gt_ct))
    print("\tSensor 3 Input = " + str(gt_ct))
    print("\tSensor 4 Input = " + str(gt_ct))
    print("\tExpected Output = \"Continue\" \r")
    result = control.choose_action(gt_ct, gt_ct, gt_ct, gt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "Continue":
        print("\tFailed!")
    else:
        print("\tPassed!")

    print("Test Scenario 16.")
    print("\tSensor 1 Input = " + str(lt_ct))
    print("\tSensor 2 Input = " + str(lt_ct))
    print("\tSensor 3 Input = " + str(lt_ct))
    print("\tSensor 4 Input = " + str(lt_ct))
    print("\tExpected Output = \"Trapped\" \r")
    result = control.choose_action(lt_ct, lt_ct, lt_ct, lt_ct, t)
    print("\tActual Output = \"" + result + "\" \r")

    if result != "Trapped":
        print("\tFailed!")
    else:
        print("\tPassed!")

if __name__ == "__main__":
    # Executes the main method only if run as a script. Will not
    # execute main() if only parts of this file are imported in
    # to another file.
    main()
