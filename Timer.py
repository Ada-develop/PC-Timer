import os

print("Simple computer shutdown timer, just write digit in minutes!")

#Shutdown function

def shutdown(arg):
        os.system("shutdown /s /t {0}".format(arg))


while True:
    #Error Handling with try/except
    while True:
        try:
            seconds = int(input("When I should to shutdown? : "));
            mins = seconds * 60
            shutdown(mins)
            break
        except ValueError:
            print("Invalid input. Write only digit in minutes!");

    #Info about shutdown:
    print("Computer will shutdown in {0} minutes.".format(mins / 60 )) # Converting minutes,to make simmilar like user input 
    
    #Cancel shutdown action:
    
    cancel = input("If you want to cancel timer just write 'cancel' ").lower();

    if cancel == "cancel":
        os.system("shutdown /a")



'''
Created by Adam Jarmolovic with love to him friend Han Gock Nguyen
(c) Adam Jarmolovic
'''

