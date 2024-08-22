
import re


text = 'We went to sunmoon went restaurant yesterday. We enjoyed a lunch there and took some rest.'

result = re.search('went', text)

# print(result) # Output: <re.Match object; span=(3, 7), match='went'>

# print(result.span()) # (3, 7)

# print(result.start()) # 3

# print(result.end()) # 7

# result = re.search('res\w*', text)

# result = re.search('r\w*', text) # Output:restaurant

# print(result.group()) # Output:restaurant


# text = 'We went to sunmoon went restaurant yesterday. We enjoyed a lunch there and took some rest.'

# result =  re.findall('r\w*', text) # ['restaurant', 'rday', 're', 'rest']

# print(result)

text = 'My favorite color or colour is Yellow.'

# text_1 = 'color or colour'

# result = re.findall(r'colou?r', text_1)

# text_2 = 'My website header color is #acd343'

# text_3 = '#fff'

# result = re.search(r'^#?([a-f0-9]{6}|[a-f0-9]{3})$', text_3)

# print(result)



import re

text = 'wrap You can wrap texts in VS code by pressing Alt+Z.'

# result = re.match(r'wrap', text) # r = raw string

# print(result) # <re.Match object; span=(0, 4), match='wrap'>



# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.fullmatch(r'You can wrap texts in VS code by pressing Alt+Z.', text)

# print(result)


# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.fullmatch(r'.*', text)

# print(result) # <re.Match object; span=(0, 48), match='You can wrap texts in VS code by pressing Alt+Z.'>


# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.search(r'.', text)

# print(result) # <re.Match object; span=(0, 1), match='Y'>


# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.findall(r'.', text)

# print(result) # ['Y', 'o', 'u', ' ', 'c', 'a', 'n', ' ', 'w', 'r', 'a', 'p', ' ', 't', 'e', 'x', 't', 's', ' ', 'i', 'n', ' ', 'V', 'S', ' ', 'c', 'o', 'd', 'e', ' ', 'b', 'y', ' ', 'p', 'r', 'e', 's', 's', 'i', 'n', 'g', ' ', 'A', 'l', 't', '+', 'Z', '.']



# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.split(r'in', text)

# print(result) # ['You can wrap texts ', ' VS code by press', 'g Alt+Z.']


# text = 'You can wrap texts in VS in code by in  pressing Alt+Z.'

# result = re.split(r'in', text, maxsplit=3)

# print(result) # ['You can wrap texts ', ' VS ', ' code by ', '  pressing Alt+Z.']


# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.sub(r'in', 'on', text)

# print(result) # You can wrap texts in VS code by pressing Alt+Z.



text = 'You can wrap texts in VS code by pressing Alt+Z. You can wrap texts in VS code by pressing Alt+Z. You can wrap texts in VS code by pressing Alt+Z. You can wrap texts in VS code by pressing Alt+Z.'


# result = re.sub(r'in', 'over', text)

# print(result)

# result = re.sub(r'in', 'over', text, count=3)

# print(result) 
# 
# # You can wrap texts over VS code by pressoverg Alt+Z. You can wrap texts over VS code by pressing Alt+Z. You can wrap texts in VS code by pressing Alt+Z. You can wrap texts in VS code by pressing Alt+Z.



text = 'You can wrap texts in VS code by pressing Alt+Z.'


result = re.finditer(r'You', text)

# print(result) # <callable_iterator object at 0x74350606bc10>

# for item in result:
#     print(item)

# print(list(result)) # [<re.Match object; span=(0, 3), match='You'>]
    

text = 'You can wrap texts in VS code by pressing Alt+Z.'


result = re.finditer(r'\b\w{4}\b', text)

# print(result) # <callable_iterator object at 0x74350606bc10>

# for item in result:
#     print(item)

# Output:
# <re.Match object; span=(8, 12), match='wrap'>
# <re.Match object; span=(25, 29), match='code'>


for item in result:
    print(item.span())
    
# Output:
# (8, 12)
# (25, 29)


# print(list(result)) 

# [<re.Match object; span=(8, 12), match='wrap'>, <re.Match object; span=(25, 29), match='code'>]


# Homework: ['wrap', 'code']



