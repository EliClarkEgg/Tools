import glob

lines = []

print("---WARNING: BE SPECIFIC AND BACK UP YOUR FILES---\n")
files = input("What file do you want to search?")
term = input("What do you want to search for?")
replacement = input("What do you want to replace it with?")

for i in glob.glob(files):
    with open(i, "r") as f:
        lines = f.read()
        if term in lines:
            lines = lines.replace(term, replacement)
            with open(i, "w") as r:
                r.write(lines)
            print(term + " replaced with " + replacement)
