import time
print('Smiley day, friend!')
time.sleep(2)
print('Would you like to solve a riddle?')
while True:                                  #start of first loop
    answer1 = input()
    if answer1 != 'yes':
        print('awwww man')
        continue
    if answer1 == 'yes':
        break                                 #end of first loop
time.sleep(2)
print("""\nSweet!! Here it goes...
        \nI am the rare case in which today comes before yesterday,
        what am I?""")
while True:                                  #starts second loop
    answer2 = input()
    if answer2 != 'dictionary':
        print('Nope, please try again!')
    if answer2 == 'dictionary':
        break                                #end of second loop
print('HUZZAH!! You solved the riddle! Thanks for playing!')



