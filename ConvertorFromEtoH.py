hebrew = "/'קראטוןםפשדגכעיחלךף,זסבהנמצתץ. "
english = "qwertyuiopasdfghjkl;'zxcvbnm,./ "

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
# The checker is probably the problem of the program  
if __name__ == '__main__':
    msg = input("Enter message to convert: ")
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

        print(msgN)
