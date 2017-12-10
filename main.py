import sys
import readchar

raw = []

with open('a.txt', 'r') as f:
    raw = f.readlines()


correct = []
wrong  = []

total = len(raw)

print 'total is : %s' % total

print 'press \'j\' or \'n\' to choose, press \'s\' to save '

def saveFile(name, cont):
    with open(name, 'a', 0) as f:
        f.writelines(cont)
        cont = []

index = 0
formerChosen = []
try:
    while index < total:
        print 'index ( %s ) now is %s' % (index, raw[index])
        
        userInput = readchar.readchar()
        print 'you choose: %s \n' % userInput
        if userInput == 'j':
            correct.append(raw[index])
            index = index + 1
        elif userInput == 'n':
            wrong.append(raw[index])
            index = index + 1
        elif userInput == 'u':
            if index == 0:
                continue
            index = index - 1
            chosen = formerChosen.pop()
            if chosen == 'j':
                correct.pop()
            elif chosen == 'n':
                wrong.pop()
            else:
                print 'noop'
        elif userInput == 's':
            saveFile('a_c.txt', correct)
            saveFile('a_w.txt', wrong)
            correct = []
            wrong = []
            print 'file saved'
        elif userInput == 'x':
            saveFile('a_c.txt', correct)
            saveFile('a_w.txt', wrong)
            print 'save and exit !'
            break
        elif userInput == 'q':
            print 'exit !'
            break
        else:
            print 'press \'j\' or \'n\' to choose '
        if userInput == 'j' or userInput == 'n':
            formerChosen.append(userInput)
except:
    print "Unexpected error:", sys.exc_info()[0]
saveFile('a_c.txt', correct)
saveFile('a_w.txt', wrong)
print 'end, save and exit !'