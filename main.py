from random import randrange

def minus(r, n):
    nums = []

    for i in range(n):
        nums.append(randrange(1, r))

        if i != n - 1:
            print(f"{nums[i]} - ", end = '')
        else:
            print(f"{nums[i]} = ?")

    answer = nums[0]
    i = 1

    while i < n - 1:
        answer -= nums[i]
        i += 1

    answer -= nums[-1]

    i = input("Your Response: ")

    if int(i) == answer:
        print("Correct")
        return

    print("Wrong...")
    print(f"Actual Answer: {answer}")


def add(r, n):
    if n == 1 or r == 1:
        print("Invalid Use Of Add Function: Both Range And Amount Of Numbers Must Be Greater Than 1")
        return

    nums = []
    answer = 0

    for i in range(n):
        nums.append(randrange(1, r))
        answer += nums[i]

        if i == n - 1:
            print(f"{nums[i]} = ?")
            continue
        print(f"{nums[i]} + ", end = '')

    i = input("Your Response: ")

    if int(i) == answer:
        print("Correct")
        return

    print("Wrong...")
    print(f"Actual Answer: {answer}")


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

    if name == "add":
        add(int(args[0]), int(args[1]))
    elif name == "minus":
        minus(int(args[0]), int(args[1]))
    else:
        print(f"Function Name: {name}")
        print(f"Function Args: {args}")


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
