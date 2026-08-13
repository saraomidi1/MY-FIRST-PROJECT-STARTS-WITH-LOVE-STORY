print("Hello, what is your name?")
name1 = input()

print(f"Hi {name1}, nice to meet you!")

print("Who is your love?")
lovename1 = input()

if lovename1 == "food":
    print("Good choice! You are a smart dude!")
elif lovename1 == "money":
    print("Smart choice! But you are a gold digger")
else:
    print("Oh... your love is really a nice person!")

print("How much do you love them?")
muchlove = input()

print("Ohhhh... that's crazy!")

correct_form = """
Better way to code:
variable_name = input("What is your name?")
print(f"Hi {variable_name}, nice to meet you!")
"""

help_1 = input("Do you want me to help you with coding? ").strip().lower()

if help_1 == "yes":
    print(correct_form)

    learned_code = input("Did you learn? ").strip().lower()

    if learned_code == "yes":
        print("Ummm... good!")
    elif learned_code == "no":
        print("Stupid! Try more!")
    else:
        print("Okay, lazy friend!")

elif help_1 == "no":
    print("Okay! Maybe next time")

