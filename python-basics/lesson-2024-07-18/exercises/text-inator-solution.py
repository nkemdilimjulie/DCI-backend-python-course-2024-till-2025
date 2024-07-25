text = input('Enter the word: ')
last_char = text[-1]
output = ''

if last_char in ['a', 'e', 'i', 'o', 'u']:
    output = text + '-inator'
else :
    output = text + 'inator'

output = output + ' ' + str(len(text)) + "000"
print(output)
