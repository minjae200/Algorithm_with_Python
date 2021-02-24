while True:
    data = input()
    if data == str(0):
        break
    if data[::-1] == data:
        print('yes')
    else:
        print('no')