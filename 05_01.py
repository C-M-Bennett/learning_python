total = 0
count = 0
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print ("Invalid input")
        continue
    count = count + 1
    total = total + fnum
print("count = " ,count)
print("total = " ,total)
print("average = " ,total/count)
print ("Done!")
