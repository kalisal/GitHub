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
