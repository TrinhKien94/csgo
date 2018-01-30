f = open("info-empire.txt", "rb")
s = f.readlines()
f.close()
f = open("info-empire-data.txt", "wb")
s.reverse()
for item in s:
  print>>f, item
f.close()
