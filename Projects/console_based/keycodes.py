from msvcrt import getch
print('enter key')
key = ord(getch())
if key == 27: #ESC
    print('esc')
elif key == 13: #Enter
        #select()
        print('enter')
##    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
##        key = ord(getch())
##        if key == 80: #Down arrow
####            moveDown()
##            print('Down arrow')
##        elif key == 72: #Up arrow
####            moveUp()
##print('Up arrow')
