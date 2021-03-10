sentence = input()
check_list = ['U', 'C', 'P', 'C']

check = True
for i in check_list:
    index = sentence.find(i)
    if index == -1:
        check = False
        break
    sentence = sentence[index+1:]
print('I love UCPC' if check else 'I hate UCPC')