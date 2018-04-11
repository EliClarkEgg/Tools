import glob

lines = []

files = input("What file do you want to search?")
term = input("What do you want to search for?")

for i in glob.glob(files):
    with open(i, "r") as f:
        lines = f.readlines()
        for n in lines:
            if term in n:
                print(term + " found in " + i + " on line " + str(lines.index(n)))
