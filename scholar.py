#!/usr/bin/env python3
import sys

def logtest():
    mark = 0
    print("the test log function is running, enter numbers for how many marks you scored per question then press enter when done")

    num = input()
    while num != "":
        mark += int(num)
        num = input()
    totalforpaper = int(input("total mark for paper: "))
    print(f"{mark}/{totalforpaper} is {mark / totalforpaper * 100}%")

    logchoice = input("log this test?[y/n] ")
    subject = input("What subject is this paper: ").lower()
    name = input("Whats the name of the test: ")
    www = input("What went well in the test: ")
    ebi = input("What could be improved from this test: ")

    if logchoice.lower() == "y":
        with open("examslog.txt", "a+") as f:
            f.write(f"{subject},{name},{mark} / {totalforpaper},good:{www},improve:{ebi}")
        print(f"{name} logged")

def trend(subject):
    pass


def progress():
    pass

def settarget():
    pass


def specificimprovements():
    pass

def feedback():
    pass


def main():
    commands = {
        "log":logtest,
    }

    command = sys.argv[0]

    if command in commands:
        commands[command]()
        if len(sys.argv) > 2:
            print("That many arguments arent supported")
