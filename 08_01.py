handle = open("mbox-short.txt")
for line in handle:
    if not line.startswith("From "): continue
    words = line.split()
    print(words[2])
