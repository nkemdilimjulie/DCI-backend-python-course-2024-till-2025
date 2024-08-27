
# Try and Except

# result = 100 / 2 # 50

# result = 100 / 0 # ZeroDivisionError: division by zero


# try:
#     result = 100 / 2
#     print(result)
# except:
#     print('This is coming from except block.')


# print('The end')

'''
50.0
The end'''


# try:
#     result = 100 / 0
#     print(result)
# except:
#     result = 100 / 20
#     print(result)
#     print('This is coming from except block.')


# print('The end')

'''
5.0
This is coming from except block.
The end'''


# try:
#     result = 100 / 30
#     print(result)
# except:
#     result = 100 / 20
#     print(result)
#     print('This is coming from except block.')


# print(f'The result is {result}')


'''
3.3333333333333335
The result is 3.3333333333333335
'''



# try:
#     result = 100 / 0
# except:
#     result = 100 / 100

# print(result)

#Output: 1.0


# try:
#     result = 100 / 0
# except Exception as e:
#     print(e)
#     result = 100 / 100

# print(result)

# division by zero
# 1.0



# try:
#     result = 100 / 0
# except ZeroDivisionError as err:
#     print(err)
#     result = 100 / 100

# print(result)


'''
division by zero
1.0'''


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)

'''
Enter a number: 50
2.0'''



# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)

'''
Enter a number: 0
division by zero'''


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)

# ValueError: invalid literal for int() with base 10: 'some text'


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except Exception as err:
#     print(err)


'''
Enter a number: 0
division by zero
dci@pc:~/.../lesson-2024-08-27$ python3 try_except.py 
Enter a number: some text
invalid literal for int() with base 10: 'some text'
'''


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

'''
Enter a number: Austria
invalid literal for int() with base 10: 'Austria'
'''

# import builtins

# print(dir(builtins))


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)
# except Exception as err:
#     print(err)

# KeyboardInterrupt


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)
# except KeyboardInterrupt as krr:
#     print(krr)
# except Exception as err:
#     print(err)
# finally:
#     print('This is the end finally.')

'''
Enter a number: 20
5.0
This is the end finally.'''

'''
Enter a number: 0
division by zero
This is the end finally.'''



# def check_age(age):
#     return f'I am {age} years old.'


# print(check_age(31))

# I am 31 years old.


# def check_age(age):
#     return f'I am {age} years old.'


# print(check_age(-25))

'''
I am 0 years old.
I am -25 years old.'''


# def check_age(age):
#     if age <= 0:
#         raise Exception
#     return f'I am {age} years old.'

# print(check_age(-25)) # Exception


def check_age(age):
    if age <= 0:
        raise Exception('Age must be a positive number.')       
    return f'I am {age} years old.'


# print(check_age(-25)) # Exception: Age must be a positive number.
# print(check_age(25)) # I am 25 years old.


# try:
#     print(check_age(25))
# except Exception as e:
#     print(e)

# I am 25 years old.

# def check_age(age):
#     if age <= 0:
#         raise Exception('Age must be a positive number.')       
#     return f'I am {age} years old.'

# try:
#     print(check_age(-25))
# except Exception as e:
#     print(e)

# Age must be a positive number.


# def check_age(age):
#     if age <= 0:
#         raise ValueError('Age must be a positive number.')       
#     return f'I am {age} years old.'

# try:
#     print(check_age(-25))
# except ValueError as e:
#     print(e)

# Age must be a positive number.


def check_age(age):
    if age <= 0:
        raise ValueError('Age must be a positive number.')       
    return f'I am {age} years old.'

try:
    print(check_age(-25))
except ValueError as e:
    print(f'An error occured: {e}')

# An error occured: Age must be a positive number.


# Dirks example:

'''
import sys
import os
  
def print_comment(comment):
  orig_stdout = sys.stdout
  try:
    f = open(os.path.basename(__file__), 'a')
    try:
      sys.stdout = f
      print( f'# {comment}....')
      sys.stdout = orig_stdout
    except:
      print("Something went wrong when opening the file")
    finally:
      f.close()
      orig_stdout = sys.stdout
  except:
      print("Something went wrong when opening the file")
      
def check_age(age):
    if age <= 0:
        raise Exception('Age mus'''


