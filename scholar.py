#!/usr/bin/env python3
import sys
import os

FILE = "examslog.txt"

def logtest():
    mark = 0
    print("the test log function is running, enter numbers for how many marks you scored per question then press enter when done")

    num = input()
    while num != "":
        mark += int(num)
        num = input()
    totalforpaper = int(input("total mark for paper: "))
    print(f"{mark}/{totalforpaper} is {mark / totalforpaper * 100}%")

    subject = input("What subject is this paper: ").lower().replace("-", ",")
    name = input("Whats the name of the test: ").lower().replace("-", ",")
    www = input("What went well in the test: ").replace("-", ",")
    ebi = input("What could be improved from this test: ").replace("-", ",")


    with open(FILE, "a+") as f:
        f.write(f"{subject}-{name}-{mark} / {totalforpaper}-good:{www}-improve:{ebi}")
    print(f"{subject} {name} logged")

def settarget():
    lines = open(FILE, "r").readlines()
    homedir = os.path.expanduser("~")

    if os.path.isfile(os.path.join(homedir, ".todolist.txt")):
        filetoaddto = os.path.join(homedir, ".todolist.txt")
    else:
        filetoaddto = "scholartgts.txt"

    subjtotgt = input("what subjects do you want to set targets for: ").lower()

    for line in lines:
        lineparts = line.split("-")
        subj = lineparts[0]

        if subjtotgt == subj.lower():
            open(filetoaddto, "a+").write(lineparts[4])
            print(f"In paper one you could do better in {lineparts[4]}, added to {filetoaddto}")



def feedback():
    lines = open(FILE, "r").readlines()
    for line in lines:
        lineparts = line.split("-")
        print(f"In {lineparts[0]}, {lineparts[1]} you got {lineparts[2]}, you did well in {lineparts[3]}, you should study up on {lineparts[4]}")


def main():
    commands = {
        "log":logtest,
        "tgt":settarget,
        "fback":feedback
    }

    command = sys.argv[1]

    if command in commands:
        commands[command]()

        if len(sys.argv) > 3:
            print("That many arguments arent supported")
    else:
        print("not a valid command")
