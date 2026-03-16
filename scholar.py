#!/usr/bin/env python3
import sys
import os
import datetime
FILE = os.path.join(os.path.dirname(__file__), "examslog.txt")

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

    time = datetime.datetime.now().strftime("%Y-%m-%d")
    open(FILE, "a+").write(f"{subject}-{name}-{mark} / {totalforpaper}-good:{www}-improve:{ebi}-{time}\n")
    print(f"{subject} {name} logged")

def settarget():
    lines = open(FILE, "r").readlines()
    homedir = os.path.expanduser("~")

    if os.path.isfile(f"{homedir}/todo/todo/.todolist.txt"):
        filetoaddto =  f"{homedir}/todo/todo/.todolist.txt"
    else:
        filetoaddto = "scholartgts.txt"

    subjtotgt = input("what subjects do you want to set targets for: ").lower()

    for line in lines:
        lineparts = line.split("-")
        subj = lineparts[0]

        if subjtotgt == subj.lower():
            if lineparts[4].strip() not in open(filetoaddto).read().splitlines():
                open(filetoaddto, "a+").write(f"In {lineparts[0]}, {lineparts[1]} you should {lineparts[4].strip()}\n")
            print(f"In {lineparts[0]}, {lineparts[1]} you could do better in {lineparts[4].strip()}, added to {filetoaddto}")

def feedback():
    lines = open(FILE, "r").readlines()
    cutoff = datetime.datetime.now() - datetime.timedelta(weeks=1)
    for line in lines:
        lineparts = line.split("-")
        if len(lineparts) < 6:
            continue
        date = datetime.datetime.strptime(lineparts[5].strip(), "%Y-%m-%d")
        if date < cutoff:
            continue
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
