
import re


text = 'We went to sunmoon went restaurant yesterday. We enjoyed a lunch there and took some rest.'

result = re.search('went', text)

print(result) # Output: <re.Match object; span=(3, 7), match='went'>

print(result.span()) # (3, 7)

print(result.start()) # 3

print(result.end()) # 7

# result = re.search('res\w*', text)

# result = re.search('r\w*', text) # Output:restaurant

# print(result.group()) # Output:restaurant


# text = 'We went to sunmoon went restaurant yesterday. We enjoyed a lunch there and took some rest.'

# result =  re.findall('r\w*', text) # ['restaurant', 'rday', 're', 'rest']

# print(result)


