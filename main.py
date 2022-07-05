from random import randrange
from os import system, name
from math import sqrt
from sys import argv

variables = {}

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def squareRoot(args):
    if len(args) != 1:
        print("Error: sqrt only accepts 1 argument")

    try:
        value = int(args[0])
    except ValueError:
        try:
            value = float(variables[args[0]])
        except:
            value = float(variables[args[0]])
    except:
        value = float(variables[args[0]])

    return sqrt(value)


def square(args):
    if len(args) != 1:
        print("Error: square only accepts 1 argument")
    try:
        value = int(args[0])
    except ValueError:
        try:
            value = float(variables[args[0]])
        except:
            value = float(variables[args[0]])
    except:
        value = float(variables[args[0]])

    return value * value

def add(args) -> int or float:
    if len(args) == 1:
        print("Invalid Use Of Add Function: Both Range And Amount Of Numbers Must Be Greater Than 1")
        return 1

    x = 0
    result = 0

    for i in args:
        try:
            result += int(i)
        except ValueError:
            try:
                result += float(variables[args[x]])
            except:
                result += float(i)
        except:
            result += float(variables[args[x]])

        x += 1

    return result


def minus(args) -> int or float:
    if len(args) == 1:
        print("Invalid use of minus: expected more than one argument")

    result = 0
    x = 0

    try:
        result = int(args[0])
    except ValueError:
        try:
            result = float(variables[args[x]])
        except:
            result = float(i)
    except:
        result = float(variables[args[x]])
    finally:
        args.pop(0)

    for i in args:
        try:
            result -= int(i)
        except ValueError:
            try:
                result -= float(variables[args[x]])
            except:
                result -= float(i)
        except:
            result -= float(variables[args[x]])
        x += 1

    return result


def times(args) -> int or float:
    if len(args) == 1:
        print("Invalid use of minus: expected more than one argument")

    result = 0
    x = 0

    try:
        result = int(args[0])
    except ValueError:
        try:
            result = float(variables[args[x]])
        except:
            result = float(i)
    except:
        result = float(variables[args[x]])
    finally:
        args.pop(0)

    for i in args:
        try:
            result *= int(i)
        except ValueError:
            try:
                result *= float(variables[args[x]])
            except:
                result *= float(i)
        except:
            result *= float(variables[args[x]])
        x += 1

    return result


def divide(args) -> int or float:
    if len(args) == 1:
        print("Invalid use of minus: expected more than one argument")

    result = 0
    x = 0

    try:
        result = int(args[0])
    except ValueError:
        try:
            result = float(variables[args[x]])
        except:
            result = float(args[0])
    except:
        result = float(variables[args[x]])
    finally:
        args.pop(0)

    for i in args:
        try:
            result /= int(i)
        except ValueError:
            try:
                result /= float(variables[args[x]])
            except:
                result /= float(i)
        except:
            result /= float(variables[args[x]])
        x += 1

    return result


def display(args):
    print(args)


def callFunction(name, args):
    result = None

    if name == "add":
        result = add(args)
    elif name == "minus":
        result = minus(args)
    elif name == "times":
        result = times(args)
    elif name == "divide":
        result = divide(args)
    elif name == "sqrt":
        result = squareRoot(args)
    elif name == "square":
        result = square(args)
    else:
        print(f"Unknown Function : {name}")
        print(f"Function Args: {args}")

    return result


class parse:
    def varName(i):
        name = []

        x = 0

        if "=" in i:
            while i[x] != "=":
                name.append(i[x])
                x += 1
            return ''.join(name)

        if ":" in i:
            x += 1

        while x < len(i):
            name.append(i[x])
            x += 1

        return ''.join(name)


    def function(i):
        nameChars = []
        args = []

        x = 0

        while i[x] != "=":
            x += 1
        x += 1

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

        value = callFunction(name, args)
        variableName = parse.varName(i)

        variables.update({variableName : value})


    def variable(i) -> str:
        if len(i) < 1:
            print("Error: Invalid Variable Value")

        name = []
        values = []

        x = 0

        while i[x] != "=":
            name.append(i[x])
            x += 1
        x += 1

        while x < len(i):
            values.append(i[x])

            x += 1

        name = ''.join(name)
        result = ''.join(values)

        if result == "?":
            result = input(" > ")

        variables.update({name : result})


def showVariable(i):
    name = parse.varName(i)
    value = str(variables.get(name))
    x = 0

    if "." in value:
        while value[x] != ".":
            x += 1
        x += 1

        if value[x] == "0":
            print(f"{name} = {int(variables.get(name))}")
            return

    try:
        print(f"{name} = {variables.get(name)}")
    except:
        print(f"Error: variable: {name} does not exist")


def shell():
    while True:
        i = input("math> ").lower().strip().replace(" ", "")

        if "#" in i  or i == "":
            pass
        elif "=" in i and "(" in i and ")" in i:
            parse.function(i)
        elif "=" in i:
            parse.variable(i)
        elif "(" in i and ")" in i:
            parse.function(i)
        elif ":" in i:
            showVariable(i)
        elif "show" in i and "." in i:
            print(variables)
        elif i == "clear":
            clear()
        elif i == "quit" or i == "q":
            return
        else:
            print(f"Error: Invalid Input")


def f(filePath):
    if ".math" not in filePath:
        print(f"Error: {filePath} is not a .math file")
        exit(1)

    parsedLines = []
    unparsedLines = []

    try:
        f = open(filePath, "r")
        for i in f:
            parsedLines.append(i.removesuffix("\n").strip().replace(" ", ""))
            unparsedLines.append(i.removesuffix("\n"))
    except:
        print(f"Error: {filePath} does not exist")
        exit(1)

    x = 0

    for i in parsedLines:
        if "#" in i  or i == "":
            pass
        elif "print" in i:
            print(unparsedLines[x][6:])
        elif "=" in i and "(" in i and ")" in i:
            parse.function(i)
        elif "=" in i:
            parse.variable(i)
        elif "(" in i and ")" in i:
            parse.function(i)
        elif ":" in i:
            showVariable(i)
        elif "show" in i and "." in i:
            print(variables)
        elif i == "clear":
            clear()
        else:
            print(f"Invalid Input: At Line {x + 1}")
            exit(1)
        x += 1

    f.close()


if __name__ == '__main__':
    argc = len(argv)

    if argc == 1:
        shell()
    else:
        f(argv[1])
else:
    print("Something went wrong make sure that this is the only python file")
