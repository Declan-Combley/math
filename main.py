from random import randrange


def minus(r, n):
    nums = []

    for i in range(n):
        nums.append(randrange(1, r))

        if i == n - 1:
            print(f"{nums[i]} = ?")
            continue
        print(f"{nums[i]} - ", end = '')

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
    nums = []
    answer = 0

    for i in range(n):
        nums.append(randrange(1, r))
        answer -= nums[i]

        if i == n - 1:
            print(f"{nums[i]} = ?")
            continue
        print(f"{nums[i]} + ", end = '')

    i = input("Your Response:  ")

    if int(i) == abs(answer):
        print("Correct")
        return

    print("Wrong...")
    print(f"Actual Answer: {answer}")

def help():
    print(" All The Available Commands:  ")
    print(" +---------------------------+")
    print(" | quit,  q  > exit          |")
    print(" | add,   +  > addition game |")
    print(" | minus, -  > addition game |")
    print(" +---------------------------+")


def main():
    while True:
        i = input("math> ").lower()

        if i == "add" or i == "+":
            add(10, 3)
        elif i == "minus" or i == "-":
            minus(10, 3)
        elif i == "quit" or i == "q":
            return
        elif i == "help":
            help()
        else:
            print("Invalid Input: Expected One Of The Following Commands")
            print(" +--------------------------------------------------+")
            print(" | quit,  q  > exit                                 |")
            print(" | add,   +  > addition game                        |")
            print(" | minus, -  > addition game                        |")
            print(" +--------------------------------------------------+")

if __name__ == '__main__':
    main()
else:
    print("Something went wrong make sure that this is the only python file")
