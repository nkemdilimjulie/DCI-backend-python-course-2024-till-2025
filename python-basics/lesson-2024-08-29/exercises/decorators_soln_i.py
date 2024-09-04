# Task 1

def make_bold(func):
    def wrapper():
        text = "<strong>"+func()+"</strong>"
        return text
    return wrapper


@make_bold
def get_html_greeting():
    return "Hello World!"

print(get_html_greeting())


# Task 2

def make_bold(func):
    def wrapper(*args, **kwargs):
        text = "<strong>"+func(*args, **kwargs)+"</strong>"
        return text
    return wrapper


@make_bold
def get_html_greeting():
    return "Hello World!"


@make_bold
def get_custom_html_greeting(first, last):
    return f"Good Day, {first} {last}!"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())


# Task 3

def make_bold(func):
    def wrapper(*args, **kwargs):
        text = "<strong>"+func(*args, **kwargs)+"</strong>"
        return text
    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        text = "<em>"+func(*args, **kwargs)+"</em>"
        return text
    return wrapper

def make_paragraph(func):
    def wrapper(*args, **kwargs):
        text = "<p>"+func(*args, **kwargs)+"</p>"
        return text
    return wrapper

@make_bold
def get_full_name(first, last):
    return first + " " + last


# @make_bold
# def get_html_greeting():
#     return "Hello World!"

@make_paragraph
@make_italic
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Good Day, {full_name}!"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))

# print(get_html_greeting())


# Task 4

def wrap_with(tag="strong"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            text = f"<{tag}>{func(*args, **kwargs)}</{tag}>"
            return text
        return wrapper
    return decorator

@wrap_with(tag="strong")
def get_full_name(first, last):
    return first + " " + last

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Good Day, {full_name}!"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))




