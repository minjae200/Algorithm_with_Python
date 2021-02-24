
array = ''
try:
    while True:
        data = input()
        array += data
except:
    array = array.split(',')
    result = 0
    for data in array:
        result += int(data)
    print(result)