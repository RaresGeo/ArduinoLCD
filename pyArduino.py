from pyfirmata import Arduino, util, STRING_DATA
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


stringList = ["Exiting", ""]

while True:
    message = input("Enter text: ")
    if message == 'exit':
        break

    lcdScrollingPrint(message)


for message in stringList:
    lcdScrollingPrint(message)
    time.sleep(max(1.5, (len(message) * 0.1)))
