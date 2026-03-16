import os
if not os.path.exists(f"{os.path.expanduser("~")}/todo"):
    open("scholartgts.txt", "w").close()
