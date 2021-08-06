name = input("Please enter your name:")
print("hello "+name)

shr = input("enter hours:")
srt = input("enter rate:")

try:
    fhr = float(shr)
    frt = float(srt)
    if fhr > 40:
        print("Overtime")
        reg = fhr * frt
        ot = (fhr-40.0)*(frt*1.5)
        #print(reg,ot)
        pay = reg + ot
    else:
        print("Regular pay")
        pay = fhr * frt
    print("Your pay is ",pay)
except:
    print("Error, please enter numeric input")
