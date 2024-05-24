mystr = input("Enter the String : ")
rev = mystr[::-1] 
if mystr == rev:
 print(f"Entered string {mystr} is palindrome")
else:
 print(f"Entered string {mystr} is not palindrome")

