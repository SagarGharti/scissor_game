import random


def gameWin(comp, you):
    if comp == you:
        c = "tie"
        return c

    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True
    elif comp == "p":
        if you == "r":
            return None
        elif you == "s":
            return True
    elif comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return None


def rand():
    print("comp Turn: Paper(p) Rock(r) or Scissor(s)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = "p"
    elif randNo == 2:
        comp = "r"
    else:
        comp = "s"
    you = input("you Turn: Paper(p) Rock(r) or Scissor(s)")
    a = gameWin(comp, you)

    print(f"computer chose {comp}")
    print(f"you chose {you}")

    if a == "tie":
        print("The game is tie")

    elif a == None:
        rand()
    elif a:
        print("you win")
    else:
        print("you lose!")


rand()
