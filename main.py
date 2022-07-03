from random import randrange


def add(args) -> int:
    if len(args) == 1:
        print("Invalid Use Of Add Function: Both Range And Amount Of Numbers Must Be Greater Than 1")
        return 1

    result = 0

    for i in args:
        result += int(i)

    print(f"Result: {result}")
    return result


def minus(args) -> int:
    if len(args) == 1:
        print("Invalid use of minus: expected more than one argument")

    answer = int(args[0])

    i = 1

    while i < len(args):
        answer -= int(args[i])
        i += 1

    print(f"Result: {answer}")
    return answer


def callFunction(name, args):
    if name == "add":
        add(args)
    elif name == "minus":
        minus(args)
    else:
        print(f"Function Name: {name}")
        print(f"Function Args: {args}")


def parseFunction(i):
    nameChars = []
    args = []

    x = 0

    while i[x] != "(":
        nameChars.append(i[x])
        x += 1
    x += 1

    name = ''.join(nameChars)

    while x < len(i) - 1:
        arg = []

        while i[x] != "," and x < len(i) - 1:
            arg.append(i[x])
            x += 1
        args.append(''.join(arg))
        x += 1


    callFunction(name, args)


def main():
    while True:
        i = input("math> ").lower().strip().replace(" ", "")

        if i[-1] == ")":
            parseFunction(i)
        elif i == "add" or i == "+":
            add(10, 3)
        elif i == "minus" or i == "-":
            minus(10, 3)
        elif i == "quit" or i == "q":
            return
        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()
else:
    print("Something went wrong make sure that this is the only python file")
