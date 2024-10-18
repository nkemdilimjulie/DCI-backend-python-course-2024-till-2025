def stack1(numb):
    div = 0
    stack2(numb, div)


def stack2(numb, div):
    compute = numb / div
    print(compute)


if __name__ == "__main__":
    numb = 5
    stack1(numb)
