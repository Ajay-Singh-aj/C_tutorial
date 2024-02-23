a=int(input("Enter your age:"))
print("your age is :",a)
print(a>18)
print(a<18)
print(a==18)
if(a>18):
    #python need indentation that we only enter into a function by some space ,we will not keep the space python 
    #understand that it is not in the function.
    print("You can drive.")
elif(a==18):
    print("you can learn how to drive")
else:
    print("You cannot drive.")
print("yey!")