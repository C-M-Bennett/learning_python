fname = input("Enter file name: ")
fhandle = open(fname)

di = dict()
for line in fhandle:
    line = line.rstrip()
    allwords = line.split()
    for word in allwords:
        di[word] = di.get(word,0) + 1
print("key then value", di)
#list of most common words and sort by values
print("value then key", sorted([(val, key) for key, val in di.items()],reverse=True))
