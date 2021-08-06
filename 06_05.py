str = 'X-DSPAM-Confidence: 0.8474 '
colpos = str.find(':')
info = str[colpos+1 : ]
print(info)
fnum = float(info)
print(fnum)
