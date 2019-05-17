num = int(input("Enter a number, -1 to stop"))
sum=0
while (num != -1):
    print ("You entered: " + str(num))
    sum= sum + num
    num = int(input("Enter a number, -1 to stop"))
print(sum)    
print ("Done.")
