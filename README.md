print("Hello, what is your name?")
name1=input()
print(f"Hi {name1}, nice to meet you!")
print("who is your love?")
lovename1=input()
if lovename1== "food":  
    print("good choice! you are smart dude!")
elif lovename1== "money":  
    print("smart choice!but you are gold digger")
else:  
  print("Oh...your love is really nice person!")
print("How much do you love them?")
muchlove=input()
print("ohhhh...that's crazy!")
print("Do you want to help you in coding?")
correct_form="""
better way to code:
variable_name=input("What is your name?")
print(f"Hi {variable_name}, nice to meet you!")
"""
help_1=input()
if help_1== "yes":
    print(correct_form)
    
learned_code=input("Did you learn?")   

if learned_code=="yes":
    print("Ummm...good!")
elif learned_code=="no":
     print("stupid!try more!")

else:
    print("ok lazy friend!")
