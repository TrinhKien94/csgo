import os
f1 = open('log_csgo500.txt','r')
log = f1.readline()
results = log.split()
black = 0
red = 0
blue = 0
gold = 0
for result in results:
    if result == 'black':
        black = black + 1
    if result == 'red':
        red = red + 1
    if result == "blue":
        blue = blue + 1
    if result == "gold":
        gold = gold + 1
while True:
    total = black+red+blue+gold
    black_base_percent = float(26)/(26+17+10+1)
    red_base_percent = float(17)/(26+17+10+1)
    blue_base_percent = float(10)/(26+17+10+1)
    gold_base_percent = float(1)/(26+17+10+1)
    black_percent = float(black)/total
    red_percent = float(red)/total
    blue_percent = float(blue)/total
    gold_percent = float(gold)/total
    black_diff = (black_percent - black_base_percent)*26
    red_diff = (red_percent - red_base_percent)*17
    blue_diff = (blue_percent - blue_base_percent)*10
    gold_diff = (gold_percent - gold_base_percent)*1
    a = []
    colors = ['black','red','blue','gold']
    print "black: "+ str(float(black)/total) +"\t"+str(black)
    print "red: "+ str(float(red)/total) +"\t"+ str(red)
    print "blue: "+ str(float(blue)/total) +"\t"+ str(blue)
    print "gold: "+ str(float(gold)/total) +"\t"+ str(gold)
    # min =  min(float(black)/26, float(red)/17,float(blue)/10,float(gold)/1)
    # print 'min: ' + str(min)
    print 'diff:'
    print 'black: '+str(black_percent-black_base_percent)
    print 'red: '+str(red_percent-red_base_percent)
    print 'blue: '+str(blue_percent-blue_base_percent)
    print 'gold: '+str(gold_percent-gold_base_percent)
    a.append(black_diff)
    a.append(red_diff)
    a.append(blue_diff)
    a.append(gold_diff)
    predict_index = a.index(min(a))
    print '\033[95mPredict color: '+colors[predict_index]+'\033[0m'
    color = raw_input("What is next color? ")
    if color == '2':
        black = black + 1
    if color == '3':
        red = red + 1
    if color == '5':
        blue = blue + 1
    if color == '50':
        gold = gold + 1
    # print float(red) - 17*min
    # print float(blue) - 10*min
    # print float(gold) - 1*min
