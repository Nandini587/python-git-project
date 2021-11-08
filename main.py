n=int(input("Enter a number:"))
temp=n
rev=0
while(n>0):
dig=num%10
rev=rev*10+dig
num=num//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("Not a palindrome")