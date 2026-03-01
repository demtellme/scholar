mark = 0
print(
    "markadder is running, enter numbers for how many marts you scored per question then press enter when done"
)

num = input()
while num != "":
    mark += int(num)
    num = input()
totalforpaper = int(input("total mark for paper: "))
print(f"{mark}/{totalforpaper} is {mark / totalforpaper * 100}%")

logchoice = input("log this test?[y/n] ")
name = input("Whats the name of the test: ")
www = input("What went well in the test: ")
ebi = input("What could be improved from this test: ")

if logchoice.lower() == "y":
    with open("examslog.txt", "a+") as f:
        f.write(f"{name},{mark} / {totalforpaper},good:{www},improve:{ebi}")
    print(f"{name} logged")
