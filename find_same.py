f = open('info-empire-data.txt','r')
s = f.readline()
def substring_indexes(substring, string):
    """
    Generate indices of where substring begins in string

    [13, 19]
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:
            break  # All occurrences have been found
        yield last_found
ss = s[1:16]
list_index =  list(substring_indexes(ss, s))
print "Find string "+ s[1:60]
count_1 = 0
count_2 = 0
count_0 = 0
for i in list_index:
    if(s[i+len(ss)] is '1'):
        count_1 = count_1 + 1
    if(s[i+len(ss)] is '2'):
        count_2 = count_2 + 1
    if(s[i+len(ss)] is '0'):
        count_0 = count_0 + 1
    print "index "+str(i)+": "+s[i+len(ss)]
print count_0
print count_1
print count_2
print "1: "+str((float)(count_1)/(count_1+count_0+count_2)*100)
print "0: "+str((float)(count_0)/(count_1+count_0+count_2)*100)
print "2: "+str((float)(count_2)/(count_1+count_0+count_2)*100)
print "done"
