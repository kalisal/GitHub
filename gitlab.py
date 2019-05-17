num = int(input("Enter a number, -1 to stop"))
sum=0
while (num != -1):
    print ("You entered: " + str(num))
    sum= sum + num
    num = int(input("Enter a number, -1 to stop"))
print ("Done.")
print(sum)
name = input("Enter a name, STOP to end")
while (name != "STOP"):
    print ("You entered: " + name)
    name = input("Enter a name, STOP to end")
print ("Done.")
'''Try-it Code 4.2 shows the diffent way to end a loop without
using user input
'''
name = input("STOP to end")
c = 0
while (name != "STOP"):
    print ("You entered: " + name)
    c = c + 1
    name = input("STOP to end")
    print ("You entered " + str (c) + " words.")
    num = int(input("Enter a number, -1 to stop"))
sum = 0
while (num != -1):
    print ("You entered: " + str(num))
    sum = sum + num
    num = int(input("Enter a number, -1 to stop"))
    print ("Sum of numbers entered: " + str (sum))
'''First loop created without the help of instrustor'''
temp =int(input("Enter the temperature (Enter a number higher than 32 to Stop)"))
total= 0
average=0
while(temp < 32):
    print(" You entered "+ str(temp))
    total= total+1
    average = average +temp #I don't know why this is read but it still runs
    temp =int(input("Enter the temperature (Enter a number higher than 32 to Stop)"))
    print(" You entered " +str(total) + " numbers")
    print("Average temperature: " + str(1.0*average/total)+" degrees")
''' 4.3 Code practe helps us to have examples of count varable and
user input used to end a loop'''
#Ex for Count variable
c = 0
while (c < 7):
    c = c + 1 #Again I don't know why this is red bit it works just fine
    print ("Python")#Ex for user input
    n = int(input ("enter #'s, -1 to stop"))
    sum = 0
while (n != -1):	
    sum = sum +n
    n = int(input ("enter #'s, -1 to stop"))
print ("Total: " + str(sum))