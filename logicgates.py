# Name : Jessiel Chasiguano.
# Course: Computer Architecture  SI-001.
print ("Welcome to the logic gates simulator.")
print ("Logic Gate Or")
x= input("Enter the value of input as 1 or 0 for x: ")
x=(int(x))
y= input("Enter the value of input as 1 or 0 for y: ")
y=(int(y))
def gate (x,y):
    if(x==0 and y==0):
        q= 0
    elif(x==1 and y==0):
        q= 1
    elif(x==0 and y==1):
        q= 1
    elif(x==1 and y==1):
        q= 1
    else:
        q="The value is not valid."
    return q
print ("The value of x is", x)
print ("The value of y is", y)     
print("The result of the gate is",gate(x,y)) 
x=0
y=0
print ("Logic Gate NAND")
x= input("Enter the value of input as 1 or 0 for x: ")
x=(int(x))
y= input("Enter the value of input as 1 or 0 for y: ")
y=(int(y))
def gate (x,y):
    if(x==0 and y==0):
        q= 1
    elif(x==1 and y==0):
        q= 1
    elif(x==0 and y==1):
        q= 1
    elif(x==1 and y==1):
        q= 0
    else:
        q="The value is not valid."
    return q
print ("The value of x is", x)
print ("The value of y is", y)     
print("The result of the gate is",gate(x,y)) 
x=0
y=0
print ("Logic Gate NOR")
x= input("Enter the value of input as 1 or 0 for x: ")
x=(int(x))
y= input("Enter the value of input as 1 or 0 for y: ")
y=(int(y))
def gate (x,y):
    if(x==0 and y==0):
        q= 1
    elif(x==1 and y==0):
        q= 0
    elif(x==0 and y==1):
        q= 0
    elif(x==1 and y==1):
        q= 0
    else:
        q="The value is not valid."
    return q
print ("The value of x is", x)
print ("The value of y is", y)     
print("The result of the gate is",gate(x,y)) 
