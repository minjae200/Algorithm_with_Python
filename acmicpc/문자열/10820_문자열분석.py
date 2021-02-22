while True:
    try:
        string = input()
    except:
        break
    if len(string) == 0: break
    upper = lower = space = digit = 0
    for i in string:
        if i.isdigit():
            digit += 1
        elif i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isspace():
            space += 1
    
    print(lower, upper, digit, space, sep=' ')