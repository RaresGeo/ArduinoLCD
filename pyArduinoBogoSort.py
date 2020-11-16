from pyfirmata import Arduino, util, STRING_DATA
import random
import time
board = Arduino('COM3')


def lcdprint(text):
    if(text):
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))
    else:
        lcdprint(" ")


def lcdScrollingPrint(text):
    if len(text) > 16 * 2:
        i = 0
        while True:
            croppedMessage = text[i:min(i + 31, len(text))]
            lcdprint(croppedMessage)
            i += 1
            if i > (len(text) - 31):
                if croppedMessage[15] == " ":
                    break
                if i > (len(text)):
                    break
            time.sleep(0.5)

    else:
        lcdprint(text)


def printArray(a):
    stringList = [str(i) for i in a]
    string = " ".join(stringList)
    lcdScrollingPrint(string)


def shuffle(a):
    for i in range(0, len(a)):
        rand = random.randint(0, len(a) - 1)
        a[i], a[rand] = a[rand], a[i]
    printArray(a)
    time.sleep(0.2)


def isSolved(a):
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True


def bogoSort(a):
    while True:
        shuffle(a)
        if isSolved(a) == True:
            break


for i in range(4, 15):
    array = []
    for j in range(0, i):
        array.append(j)
        print(array)

    bogoSort(array)

    time.sleep(2)
