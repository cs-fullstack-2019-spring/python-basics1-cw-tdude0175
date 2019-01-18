def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

'''
Create a function with two variables. 
One should equal “My name is: “ 
and the other should equal your actual name. 
Print the two variables in one print message.
'''

def problem1():
    myNameIs =("My name is: ")
    name = ("Thomas")
    print(myNameIs + name)

'''
Create a function to ask the user to enter the extra credit they earned. 
If they entered less than 5 print “That’s not enough extra credit.” 
If they entered more than 20 print “That’s too much extra credit”.
'''

def problem2():
    extraCredit = int(input("How much credit did you earn"))
    if(extraCredit < 5):
        print("That’s not enough extra credit.")
    elif(extraCredit > 20):
        print("That’s too much extra credit.")

'''
Create a function to ask a user to enter a password. 
Enter a password. 
Ask user to reenter password. 
Check to see if they are correct.
'''

def problem3():
    secretPassword =("C0d3Cr3w")
    userInput = input("enter password")
    if(userInput == secretPassword):
        print("welcome")
    else:
        print("Access denied")

'''
Create a function to ask for two card numbers. 
If it equals 21 print BLACKJACK!, 
if it’s greater than 21 print BUST!, 
if it’s less than 21 print “The total is [THE TOTAL]”
'''

def problem4():
    card1 = int(input("whats your first cards count?"))
    card2 = int(input("what is the count of your second count"))
    if(card1+card2 == 21):
        print("blackjack")
    elif(card1+card2 > 21):
        print("Bust")
    else:
        print("Your total is " +str(card1+card2))

if __name__=='__main__':
    main()

