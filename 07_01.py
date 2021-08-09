fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    sline = line.rstrip()
    print(sline.upper())
