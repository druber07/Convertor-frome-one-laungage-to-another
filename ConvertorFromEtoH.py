hebrew = "/'קראטוןםפשדגכעיחלךף,זסבהנמצתץ. "
english = "qwertyuiopasdfghjkl;'zxcvbnm,./ S"

def convHeEn(msg):
    msgN = ''
    for char in msg:
        print(hebrew.index(char), char)
        msgN += english[hebrew.index(char)]

    return msgN

def convEnHe(msg):
    msgN = ''
    for char in msg:
        msgN += hebrew[english.index(char)]

    return msgN[::1]

def launguage(msg):
    ask = True

    def Eng(msg):
        for let in msg:
            letterIf = True
            for LEng in english:
                if let != LEng:
                    letterIf = False
                else:
                    letterIf = True

            if  not letterIf:
                return False
        return True

    def Rus(msg):
        for let in msg:
            letterIf = True
            for LEng in english:
                if let != LEng:
                    letterIf = False
                else:
                    letterIf = True

            if  not letterIf:
                return False
        return True
        
    def Heb(msg):
        for let in msg:
            letterIf = True
            for LEng in english:
                if let != LEng:
                    letterIf = False
                else:
                    letterIf = True

            if  not letterIf:
                return False
        return True
        
        
    if Eng(msg):
        print('That is english')
    elif Heb(msg):
        print('That is hebrew')

if __name__ == '__main__':
    msg = input("Enter message to convert:\n")
    launguage(msg)

"""""
if(msg[-1] == x for x in english):
        print("That's english")
        msgN = ''
        for char in msg:
            msgN += hebrew[english.index(char)]

        print(msgN[::-1])
    elif (msg[-1] == x for x in hebrew):
        print("That's hebrew")
        msgN = ''
        for char in msg:
            msgN += english[hebrew.index(char)]
"""