a=int(input("Enter any number:"))
if a>1:
    for x in range(2,a):
        if(a%x)==0:
            print("Its not a prime number")
            break
        else:
            print("Its a prime number")
            break
else:
    print("Not Prime")