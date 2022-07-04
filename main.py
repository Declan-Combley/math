from random import randrange

variables = {}

def showVariable(i):
    print(f"{i[1]} = {variables[i[1]]}")


def add(args) -> int:
    if len(args) == 1:
        print("Invalid Use Of Add Function: Both Range And Amount Of Numbers Must Be Greater Than 1")
        return 1

    x = 0
    result = 0

    for i in args:
        try:
            result += int(i)
        except:
            result += int(variables[args[x]])
        finally:
            x += 1

    print(f"Result: {result}")
    return result


def minus(args) -> int:
    if len(args) == 1:
        print("Invalid use of minus: expected more than one argument")

    result = 0
    x = 0

    try:
        result = int(args[0])
    except:
        result = int(variables[args[x]])
    finally:
        args.pop(0)

    for i in args:
        try:
            result -= int(i)
        except:
            result -= int(variables[args[x]])
        finally:
            x += 1

    print(f"Result: {result}")
    return result


def callFunction(name, args):
    result = None

    if "add" in name:
        result = add(args)
    elif name == "minus":
        result = minus(args)
    else:
        print(f"Unknown Function : {name}")
        print(f"Function Args: {args}")

    return result

class parse:
    def function(i):
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

        return callFunction(name, args)

    def variable(i) -> str:
        x = 2
        values = []

        while x < len(i):
            values.append(i[x])
            x += 1

        result = ''.join(values)

        return result


def main():
    while True:
        i = input("math> ").lower().strip().replace(" ", "")

        if "=" in i and "(" in i and ")" in i:
            result = parse.function(i[2:])
            variables[i[0]] = result
        elif "=" in i:
            variables.update({i[0] : parse.variable(i)})
        elif "(" in i and ")" in i:
            parse.function(i)
        elif i[0] == ":":
            showVariable(i)
        elif "show" in i and "." in i:
            print(variables)
        elif i == "quit" or i == "q":
            return
        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()
else:
    print("Something went wrong make sure that this is the only python file")
