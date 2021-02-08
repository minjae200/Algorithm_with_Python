string = input()
bigA, bigZ = ord('A'), ord('Z')
smallA, smallZ = ord('a'), ord('z')

for char in string:
    data = ord(char)
    if bigA <= data <= bigZ:
        encryption = data + 13
        if encryption > bigZ:
            encryption = encryption - bigZ + bigA - 1
        print(chr(encryption), end='')
    elif smallA <= data <= smallZ:
        encryption = data+ 13
        if encryption > smallZ:
            encryption = encryption - smallZ + smallA -1
        print(chr(encryption), end='')
    else:
        print(char, end='')