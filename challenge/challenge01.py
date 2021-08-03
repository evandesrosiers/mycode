#!/usr/bin/env python3
#Evan Sean DesRosiers

def main():
    answer = " "
    print("What is the Ultimate Quesiton")
    answer = input("The answer is 42 print\nA: How many roads must a man walk down?\nB: How many Vogons does it take to change a light bulb?\nC: What is 6 times 7?\nD: INSUFFICIENT DATA FOR MEANINGFUL ANSWER\n")
    if answer == "a":
        print("Arthur Dent, is that you? GO AWAY!")
    elif answer == "b":
        print("Only one actually, but only after the paperwork has been filed in triplicate.")
    elif answer == "c":
        print("If I wanted a calculator I would've just opened the calculator.")
    elif answer == "d":
        print("Different author but the right mindset.")
    else:
        print("How hard is it to type one letter?")

main()
