"""Write a simple ATM program. Ask the user to enter their account number, 
and then print their beginning balance. (Just make one up). 
If the account number is wrong, 
they should be prompted to reenter it. 
Then ask them if they want to make a deposit or a withdrawal. 
If deposit is chosen, deposit the amount they entered, 
then print the new balance. 
Alternatively, if they choose to withdraw, withdraw 
the amount they entered 
IF they have the balance to do so, then print the new balance. 
They should be able to do as many transactions as they wish, 
so use iteration here.
"""
acnum= (int(input("Enter your account Number")))
while(acnum != 5678):
    acnum = int(input("Sorry Wrong, try again"))
if(acnum == 5678):
    print("Your balance is " + str(1200.00))
answer=(input("Do you want to deposit or withdraw? (If nothing enter Nope)"))
if(answer == "deposit"):
    deposit=float(input(" How much do you want to add"))
    print("Your current balance is "+str(1200.00 + deposit))
    newbalanced=1200.00 + deposit
    answer2=(input("Do you wish continue? (If not enter Nope)"))
    if (answer2 == "yes" or answer2== "Yes"):
        answer4=input(" Would You like to deposit or withdraw")
    if(answer4 == "deposit"):
        addmore=(float(input("How much do you want to deposit (Enter negstive number to Stop")))
        while(addmore >0):
            newbalanced= newbalanced + addmore
            addmore=(float(input("How much do you want to deposit (Enter negstive number to Stop)")))
            print( "Now Your balance is $"+str(newbalanced))
    else:
        submore= (float(input("How much do you want to withdraw (Enter a Negative Number to Stop"))) 
        while (submore > 0):
            newbalanced = newbalanced - submore
            submore= (float(input("How much do you want to withdraw (Enter a Negative Number to Stop")))
            print( "Now Your balance is $"+str(newbalanced))
if( answer== "withdraw"):
        withdraw=(float(input(" How much do you want withdraw?")))
        if (withdraw > 1200.00):
                    print(" Sorry invalid. Enter Your Pin Number Again")
        elif(withdraw <= 1200.00):
                    print(" Your current balance is now "+str(1200.00 - withdraw))
                    newbalancew= 1200.00 - withdraw
        answerw1=(input("Do wish to continue? (If not enter Nope)"))
        if (answerw1== "yes" or answerw1== "Yes"):
            answerw2=input(" Would You like to deposit or withdraw")
            if(answerw2 == "deposit"):
                addmorew=(float(input("How much do you want to deposit (Enter negstive number to Stop")))
                while(addmorew >0):
                    newbalancew= newbalancew + addmorew
                    addmorew=(float(input("How much do you want to deposit (Enter negstive number to Stop)"))) 
                    print("Now Your balance is $"+str(newbalancew))
            else:
                submorew= (float(input("How much do you want to withdraw (Enter a Negative Number to Stop")))
                while (submorew > 0):
                    newbalancew = newbalancew - submorew
                    submorew= (float(input("How much do you want to withdraw (Enter a Negative Number to Stop")))
                    print( "Now Your balance is $"+str(newbalancew))