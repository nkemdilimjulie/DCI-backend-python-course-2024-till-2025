def check_for_even(string_to_check):
    if len(string_to_check) % 2 == 0 :
        print(string_to_check + " --> even")
    else :
        print(string_to_check + " --> odd")


input1 =  'hello world'
input2  = 'hello planet'
input3  = ''

check_for_even(input1)
check_for_even(input2)
check_for_even(input3)
