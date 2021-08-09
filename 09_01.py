fname = input("Enter file name: ")
fhandle = open(fname)

di = dict()
for line in fhandle:
    line = line.rstrip()
    allwords = line.split()
    for word in allwords:
        #if word in di:
            #di[word] = di[word] + 1
        #else:
            #di[word] = 1
        #replace above code with below
        di[word] = di.get(word,0) + 1
print(di)
