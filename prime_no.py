# Enter a number and check whether its prime or not 
num=int(input("Enter a number"))
i=2
end=num//2
c=0
while i<=end:
  if num%i==0:
    c+=1
    i+=1
  else:
    i+=1
    continue
if c==0:
  print("Its a prime numer")
elif c>0:
  print("Its not a prime numer ")
else:
  print("Invalid")
